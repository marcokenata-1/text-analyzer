import json

def merge_lists(l1, l2):
    return sorted(list(set(l1 + l2)))

def main():
    try:
        with open("data/mappings/gics_ifrs_mapping_finbert.json", "r") as f:
            finbert = json.load(f)
    except FileNotFoundError:
        print("Warning: finbert json not found")
        finbert = {}
        
    try:
        with open("data/mappings/gics_ifrs_mapping_ollama.json", "r") as f:
            ollama = json.load(f)
    except FileNotFoundError:
        print("Warning: ollama json not found")
        ollama = {}
        
    merged = {}
    all_keys = set(list(finbert.keys()) + list(ollama.keys()))
    
    for k in all_keys:
        f_data = finbert.get(k, {})
        o_data = ollama.get(k, {})
        
        name = f_data.get("name") or o_data.get("name")
        universal = merge_lists(f_data.get("universal_tags", []), o_data.get("universal_tags", []))
        sector = merge_lists(f_data.get("sector_tags", []), o_data.get("sector_tags", []))
        ifrs = merge_lists(universal, sector)
        
        merged[k] = {
            "name": name,
            "universal_tags": universal,
            "sector_tags": sector,
            "ifrs_tags": ifrs
        }
        
    # Sort dict by keys to make it consistent
    merged = dict(sorted(merged.items()))
        
    with open("data/mappings/gics_ifrs_mapping_merged.json", "w") as f:
        json.dump(merged, f, indent=2)
    print("Merged JSON saved to gics_ifrs_mapping_merged.json")

if __name__ == "__main__":
    main()
