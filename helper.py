import re
import json
import datetime
import requests



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
    except FileNotFoundError, json.JSONDecodeError:
        print(f"Error: {filepath} does not exist or the JSON cache file is corrupted.")
        return None

def check_response(response):
    if response.status_code != 200:
        print(f"Error: An error occured, status code: {response.status_code}, check your internet connection.")
        return
    try:
        return response.json()
    except json.JSONDecodeError:
        print("Error: Recieved bad response, cant convert to JSON")
        return None

def get_response(endpoint, filepath, parameter, query, header= None):
    if not header:
        response = requests.get(endpoint, params=parameter, timeout = 5)
    elif header:
        response = requests.get(endpoint, params=parameter, headers=header, timeout = 5)
    response = check_response(response)
    if response == None:
        print("Error: No results")
        return
    if not header:
        response['search'] = query.lower().strip()
        response['dateCreated'] = str(datetime.date.today())
    elif header:
        response.append(
            {
            'search': query.lower().strip(), 
            'dateCreated': str(datetime.datetime.now())
            }
        )
        response
    with open(filepath, "w", encoding="utf-8") as file:
            json.dump(response, file, indent=4)
    return