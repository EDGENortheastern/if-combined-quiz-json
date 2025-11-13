# storage.py
import json
from pathlib import Path
from datetime import datetime

RESULTS_FILE = Path("results.json")


def load_results() -> list[dict]:
    """
    Load all saved quiz results from JSON.
    Returns an empty list if the file does not exist yet.
    """
    if RESULTS_FILE.exists():
        with RESULTS_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_result(name: str, score: int) -> None:
    """
    Append a single result (name, score, date) to results.json.
    """
    results = load_results()

    results.append(
        {
            "name": name,
            "score": score,
            "date": datetime.now().isoformat(timespec="seconds"),
        }
    )

    with RESULTS_FILE.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
