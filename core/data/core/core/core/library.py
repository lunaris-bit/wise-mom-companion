import json
import os

# NOTE: wise_mom_library.json adalah sumber data utama Wise Mom Library.
LIBRARY_PATH = "data/wise_mom_library.json"

def load_library():
    if not os.path.exists(LIBRARY_PATH):
        return []
    with open(LIBRARY_PATH, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def find_library_case(query):
    # Placeholder: Belum ada logika pencarian
    return None
