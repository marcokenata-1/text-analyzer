"""
Converts Layer 1 extractions.json to a flat list of LineItems.

Each document has a 'tables' list; tables have 'headers' and 'rows', both
full of empty-string cells from merged-cell PDF rendering. We keep only
tables whose headers name a description column and whose rows contain a
financial keyword, then per row skip empty/year/percentage/single-char
cells to find the description and take the first numeric value after it
as the most-recent-year amount. Descriptions are de-duplicated across
tables since statements often repeat summary lines.

extract_company_name() tries, in order: Layer 1's own doc["company_name"],
an exchange ID lookup (filename + source -> DuckDuckGo), boilerplate
phrases like "performance of Acme Corp during the year" in the first 3
tables, then the most-frequent Title Case phrase across the first 5
tables as a last resort.
"""

import re
import requests
from typing import Optional


FINANCIAL_TERMS = re.compile(
    r'\b(assets?|liabilities?|equity|revenue|sales?|profit|loss|income|expense|'
    r'cost|cash|capital|earnings?|financing|investing|operating|comprehensive|'
    r'receivable|payable|inventory|goodwill|depreciation|amortization|'
    r'zakah|zakat|dividend|shareholders?|borrowings?|debt|interest|tax(?:es)?|'
    r'provisions?|impairment|write.?off|retained|reserves?|surplus|deficit)\b',
    re.I,
)

DESCRIPTION_HEADERS = re.compile(
    r'\b(statement|description|particulars|item|details?|notes?)\b', re.I
)

YEAR_RE     = re.compile(r'^\d{4}$')
PCT_RE      = re.compile(r'^-?[\d,\.]+\s*%$')
NUMBER_RE   = re.compile(r'^-?[\d,]+\.?\d*$')
FRAGMENT_RE = re.compile(r'^(and|or|the|of|in|for|to|a|at|by|as|on)\s*$', re.I)

# Filename convention: {company_id}_{revision}_{fiscal_year_end}_{time}_{lang}.pdf
_FILENAME_ID = re.compile(r'^(\d+)_')

# Maps source tag → DuckDuckGo search prefix used to resolve a numeric company ID
_EXCHANGE_QUERIES = {
    'saudi_exchange': 'Saudi Exchange Tadawul company {id}',
    'tadawul':        'Saudi Exchange Tadawul company {id}',
    # extend for other exchanges as needed
}


def _company_id_from_doc(doc: dict) -> tuple[Optional[str], Optional[str]]:
    """Return (company_id, source) parsed from the document metadata, or (None, None)."""
    filename = doc.get('filename', '')
    source   = doc.get('source', '')
    m = _FILENAME_ID.match(filename)
    if m and source in _EXCHANGE_QUERIES:
        return m.group(1), source
    return None, None


def _lookup_company_by_id(company_id: str, source: str) -> Optional[str]:
    """
    Query DuckDuckGo Instant Answer with a source-specific search string to
    resolve a numeric exchange company ID to a company name.
    Returns the first recognisable company name from the abstract or related
    topics, or None if the search yields nothing useful.
    """
    query = _EXCHANGE_QUERIES[source].format(id=company_id)
    try:
        resp = requests.get(
            'https://api.duckduckgo.com/',
            params={'q': query, 'format': 'json', 'no_html': '1', 'skip_disambig': '1'},
            timeout=5,
        )
        data = resp.json()
        abstract = data.get('AbstractText', '').strip()
        if abstract:
            return abstract.split('.')[0].strip()
        for topic in data.get('RelatedTopics', []):
            text = topic.get('Text', '').strip()
            if text:
                return text.split('.')[0].strip()
    except Exception:
        pass
    return None


# Boilerplate phrases in annual report TOC/intro tables that precede the company name
_INTRO_PHRASE = re.compile(
    r'(?:performance of|report of|directors? of|annual report of|statements? of|'
    r'activities of|overview of|results? of|prepared by|issued by|submitted by)\s+'
    r'((?:[A-Z][A-Za-z&\-]+\s+){1,6})',
    re.UNICODE,
)

# Words that are NOT part of a company name even when Title Case
_STOP_WORDS = frozenset({
    'The', 'A', 'An', 'In', 'Of', 'For', 'And', 'Or', 'To', 'By', 'At',
    'On', 'With', 'From', 'During', 'Until', 'About', 'As', 'Is', 'It',
    'This', 'That', 'These', 'Those', 'Which', 'Who', 'Its', 'Their',
    'General', 'Annual', 'Fiscal', 'Year', 'Board', 'Company',
    'Financial', 'Statement', 'Report', 'Page', 'Total', 'Saudi',
    'Kingdom', 'First', 'Second', 'Third', 'Fourth',
})

_TITLE_RUN = re.compile(r'[A-Z][A-Za-z&\-]+')


def clean_amount(raw: str) -> Optional[str]:
    """'1,234,567' → '1234567';  '(1,234)' → '-1234';  else None."""
    v = raw.strip().replace(',', '').rstrip('.')
    if v.startswith('(') and v.endswith(')'):
        v = '-' + v[1:-1]
    try:
        float(v)
        return v
    except ValueError:
        return None


def is_skip_cell(cell: str) -> bool:
    c = cell.strip()
    return (
        not c
        or YEAR_RE.match(c)
        or PCT_RE.match(c)
        or FRAGMENT_RE.match(c)
        or len(c) <= 1
    )


def first_description(cells: list[str]) -> Optional[str]:
    """Return first cell that looks like a financial line-item description."""
    for c in cells:
        c = c.strip()
        numeric_form = c.replace(',', '').replace('(', '').replace(')', '')
        if not is_skip_cell(c) and not NUMBER_RE.match(numeric_form):
            return c
    return None


def first_amount_after(cells: list[str], desc: str) -> Optional[str]:
    """Return the first parseable numeric cell that appears after desc in the row."""
    past_desc = False
    for c in cells:
        c = c.strip()
        if not past_desc:
            if c == desc:
                past_desc = True
            continue
        amt = clean_amount(c)
        if amt is not None:
            return amt
    return None


def _all_table_text(tables: list, limit: int) -> list[str]:
    """Collect all non-empty cell strings from the first `limit` tables."""
    texts = []
    for t in tables[:limit]:
        for row in t.get('rows', []):
            for cell in row:
                s = str(cell).strip()
                if s:
                    texts.append(s)
    return texts


def extract_company_name(doc: dict) -> Optional[str]:
    """
    Four-tier company name detection, generic across any annual report;
    see the module docstring for the tier order. Tier 4 (frequency-based)
    excludes same-word repeats from prose ("CGUs CGUs") and repeated
    whole-cell structural labels ("Outside KSA" in a disclosure table), but
    is still unreliable on documents dominated by governance boilerplate or
    heavy mentions of a counterparty, so treat its result as a guess.
    """
    # Tier 1
    if doc.get('company_name'):
        return doc['company_name'].strip()

    # Tier 2: exchange company ID lookup
    company_id, source = _company_id_from_doc(doc)
    if company_id and source:
        name = _lookup_company_by_id(company_id, source)
        if name:
            return name

    tables = doc.get('tables', [])

    # Tier 3: boilerplate phrase scan
    for text in _all_table_text(tables, limit=3):
        m = _INTRO_PHRASE.search(text)
        if m:
            name = m.group(1).strip().rstrip('.,;:')
            if len(name) > 3:
                return name

    # Tier 4: most-frequent Title Case run (2+ consecutive qualifying words)
    from collections import Counter
    cell_texts = _all_table_text(tables, limit=5)
    # A phrase that IS a whole cell, where that exact cell recurs, is a
    # repeated structural label (e.g. "Outside KSA" in a board-membership
    # disclosure table) rather than a name mentioned in running prose.
    whole_cell_counts = Counter(cell_texts)

    counts: Counter = Counter()
    for text in cell_texts:
        words = _TITLE_RUN.findall(text)
        # Build all consecutive sub-sequences of 2+ non-stop words
        clean = [w for w in words if w not in _STOP_WORDS]
        for length in (3, 2):
            for i in range(len(clean) - length + 1):
                chunk = clean[i:i + length]
                if len(set(chunk)) < len(chunk):
                    continue  # reject same-word repeats, e.g. "CGUs CGUs"
                phrase = ' '.join(chunk)
                if text == phrase and whole_cell_counts[text] >= 3:
                    continue  # reject repeated structural label values
                counts[phrase] += 1
    if counts:
        best, freq = counts.most_common(1)[0]
        if freq >= 2:
            return best

    return None


def _is_financial_table(headers: list[str], rows: list) -> bool:
    if not any(DESCRIPTION_HEADERS.search(h) for h in headers):
        return False
    all_text = ' '.join(str(cell) for row in rows for cell in row if cell)
    return bool(FINANCIAL_TERMS.search(all_text))


def parse_extractions(data: dict) -> tuple[Optional[str], list[dict]]:
    """
    Parse extractions.json.

    Returns:
        company_name: auto-detected via four-tier heuristic (see extract_company_name)
        items:        flat list of {id, description, amount} dicts
    """
    items: list[dict] = []
    seen: set[str] = set()
    seen_lower: set[str] = set()
    item_id = 1
    company_name: Optional[str] = None

    for doc in data.get('documents', []):
        if company_name is None:
            company_name = extract_company_name(doc)

        for table in doc.get('tables', []):
            headers = [str(h).strip() for h in table.get('headers', [])]
            rows    = table.get('rows', [])

            if not _is_financial_table(headers, rows):
                continue

            for row in rows:
                cells = [str(c) for c in row]

                desc = first_description(cells)
                if not desc:
                    continue
                if desc in seen or desc.lower() in seen_lower:
                    continue
                if not FINANCIAL_TERMS.search(desc):
                    continue

                amt = first_amount_after(cells, desc)
                if amt is None:
                    continue

                seen.add(desc)
                seen_lower.add(desc.lower())
                items.append({'id': item_id, 'description': desc, 'amount': amt})
                item_id += 1

    return company_name, items
