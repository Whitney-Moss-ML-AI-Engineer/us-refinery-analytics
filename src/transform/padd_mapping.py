import json
from pathlib import Path

CONFIG = Path("config/padd_mapping.json")

def load_padd_map():
    data = json.loads(CONFIG.read_text())
    return {state: padd for padd, states in data.items() for state in states}

def assign_padd(state: str) -> str | None:
    return load_padd_map().get(state.upper().strip())
