import re
import json


def check_char_validity(query):
    pattern = r"^[\w\-\. ]+$"
    if match := re.search(pattern, query, re.ASCII):
        return True
    else:
        return False

def load_cache_data(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filepath} does not exist")
        return None