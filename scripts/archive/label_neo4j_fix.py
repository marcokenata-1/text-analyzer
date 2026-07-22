"""
Fix IFRSTag labels in Neo4j — labels were stored as tag names instead of
human-readable labels from the XML file.

Run this after load_neo4j.py to patch the label property.
"""

import xml.etree.ElementTree as ET
from neo4j import GraphDatabase

URI      = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"
DB       = "ifrs-gics"


import re

def camel_to_sentence(name: str) -> str:
    """Convert CamelCase tag name to readable sentence."""
    # Insert space before uppercase letters that follow lowercase letters
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
    # Insert space before uppercase letters followed by lowercase (e.g. IFRSTag → IFRS Tag)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
    return s.strip()


def parse_labels():
    """Parse human-readable labels from IFRS label XML using id attribute."""
    label_map = {}
    tree = ET.parse("data/taxonomy/lab_full_ifrs-en_2025-03-27.xml")
    root = tree.getroot()
    ns   = {"link": "http://www.xbrl.org/2003/linkbase"}

    for label in root.findall(".//link:label", ns):
        id_attr = label.get("id", "")
        text    = label.text or ""

        # Pattern: ifrs-full_TagName_label
        if (id_attr.startswith("ifrs-full_")
                and id_attr.endswith("_label")
                and text
                and "[" not in text):  # skip abstract/axis/domain entries
            tag = id_attr[len("ifrs-full_"):-len("_label")]
            if tag not in label_map:
                label_map[tag] = text

    return label_map


def fix_labels():
    print("Parsing labels from XML...")
    label_map = parse_labels()
    print(f"  Found {len(label_map)} labels")

    # Check a few samples
    samples = [
        "AccrualsAndDeferredIncomeIncludingContractLiabilities",
        "LoansAndAdvancesToCustomers",
        "Assets",
        "Revenue",
        "CashAndCashEquivalents",
    ]
    print("\nSample label lookups:")
    for tag in samples:
        label = label_map.get(tag, "NOT FOUND")
        print(f"  {tag[:50]:50s} → {label}")

    print("\nUpdating Neo4j labels...")
    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

    with driver.session(database=DB) as session:
        # Get all IFRSTag nodes
        result  = session.run("MATCH (t:IFRSTag) RETURN t.name AS name")
        tags    = [row["name"] for row in result]
        print(f"  Found {len(tags)} IFRSTag nodes to update")

        updated = 0
        fallback = 0
        skipped  = 0
        for tag in tags:
            label = label_map.get(tag)
            if label and label != tag:
                # Use proper XML label
                session.run(
                    "MATCH (t:IFRSTag {name: $name}) SET t.label = $label",
                    name=tag, label=label
                )
                updated += 1
            else:
                # Fallback — convert CamelCase to readable sentence
                readable = camel_to_sentence(tag)
                session.run(
                    "MATCH (t:IFRSTag {name: $name}) SET t.label = $label",
                    name=tag, label=readable
                )
                fallback += 1

        print(f"  Updated (XML label):      {updated}")
        print(f"  Updated (camelCase fix):  {fallback}")

    driver.close()

    print("\nVerifying fix — sample Financials tags:")
    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))
    with driver.session(database=DB) as session:
        result = session.run("""
            MATCH (s:Sector {code: '40'})-[:MAPS_TO]->(t:IFRSTag)
            WHERE t.label <> t.name
            RETURN t.name AS name, t.label AS label
            ORDER BY t.name
            LIMIT 15
        """)
        for row in result:
            print(f"  {row['name'][:45]:45s} → {row['label']}")

    driver.close()
    print("\n✅ Labels fixed!")


if __name__ == "__main__":
    fix_labels()