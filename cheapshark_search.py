import requests
import json
import config
import helper
from pathlib import Path
from sys import exit


def main():
    while True:
        query = input("Title (Q to quit): ")
        if query.strip().lower() == 'q':
            exit("Thank you for using my app.")
        validity = helper.check_char_validity(query)
        if validity:
            search(query)
            break
        elif not validity:
            print("Letters, numbers, dash, underscore, and dot characters for the query only.")
    return None

class Game_Deals:
    def __init__(self, title, normal_price, store_price):
        self.title = title
        self.normal = normal_price
        self.store = store_price
    def display(self):
        print(f"""
Title: {self.title}
Normal Price: {self.normal}
Store Prices:""")
        self.store_names()

    def store_names(self):
        for i, (store, price) in enumerate(self.store.items(), 1):
            if store in config.cheapshark_store_map:
                print(f"""{i}. {config.cheapshark_store_map[store]} = {price}""")


def search(query):
    filepath = Path(Path(__file__).parent / "Cheapshark_cache" / f"{query.strip().lower()}.json")
    folder = filepath.parent

    if not filepath.exists():
        folder.mkdir(parents=True, exist_ok=True)
        parameters = {
            'title': query.strip(),
        }

        response = requests.get(config.cheapshark_url + "deals", headers=config.headers, params=parameters, timeout = 10)

        response = req_cheapshark_data(response)
        if response == None:
            print("No results")
            return
        response.append({'search': query.lower().strip()})

        with open(filepath, "w") as file:
            json.dump(response, file, indent=4)

        data = helper.load_cache_data(filepath)
        if data == None:
            print(f"No results from {filepath.name} cached data")
            return
        
        store_price = check_prices_store(data)
        display(store_price)
    
        print("No JSON exists")
    elif filepath.exists():
        data = helper.load_cache_data(filepath)

        if data == None:
            print(f"No results from {filepath.name} cached data")
            return
        store_price = check_prices_store(data)
        display(store_price)
        print("JSON exists")


def req_cheapshark_data(response):
    if response.status_code != 200:
        print(f"Error: An error occured, status code: {response.status_code}, check your internet connection.")
        return
    try:
        return response.json()
    except json.JSONDecodeError:
        print("Error: Recieved bad response, cant convert to JSON")
        return None

def check_prices_store(data):
    lst = []
    seen_titles = set()

    for item in data:
        if 'title' not in item:
            continue
        if item['title'] not in seen_titles:
            lst.append({'title': item['title'], 'normalPrice': item['normalPrice'], 'stores': {}})
            seen_titles.add(item['title'])

        for game in lst:
            if game['title'] == item['title']:
                game['stores'][item['storeID']] = item['salePrice']
    return lst


def display(lst):
    for item in lst:
        deals = Game_Deals(item['title'], item['normalPrice'], item['stores'])
        deals.display()


if __name__ == "__main__":
    main()