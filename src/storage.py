import json
import os

DATA_FILE = os.path.join("data", "students.json")


def ensure_storage():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def load_students():
    ensure_storage()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_students(students):
    ensure_storage()
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)
