import requests
import json
import re
import config
from sys import exit
import helper
from pathlib import Path

storeids = [1,3,7,6,11]


def main():
    while True:
        query = input("Title (Q to quit): ")
        if query.strip().lower() == 'q':
            exit("Thank you!")
        validity = helper.check_char_validity(query)
        if validity:
            search(query)
            break
        elif not validity:
            print("Letters, numbers, dash, underscore, and dot characters for the query only.")
    return None


class Game:
    def __init__(self, name, release_date, stores, cheapest):
        self.name = name
        self.release = release_date
        self.price = cheapest
        self.stores = stores
    def display(self):
        print(f"""
Game Name: {self.name}
Release Date: {self.release}
Cheapest Price: {self.price}   
Stores:""")
        for i, store in enumerate(self.stores, 1):
            print(f"""{i}. {store}""")

def search(query):
    cache_file = Path(Path(__file__).parent / "Rawg_cache" / f"{query.lower().strip()}.json")
    folder = cache_file.parent

    if not cache_file.exists():
        folder.mkdir(parents=True, exist_ok = True)

        parameter = {
            'key': config.RAWG_API,
            'search': query,
            'search_precise': True,
        }

        response = requests.get(config.rawg_url + "games", params=parameter, timeout = 5)
        
        response = req_rawg_data(response)
        if response == None:
            print("Error: No results")
            return

        response['search'] = query.lower().strip()

        with open(cache_file, "w", encoding="utf-8") as file:
            json.dump(response, file, indent=4)

        display_results(response)
        print("Json does not exits, 1 response burned")

    elif cache_file.exists():
        data = helper.load_cache_data(cache_file)

        if data is None:
            print(f"Error: {cache_file.name} yielded no result")
            return

        display_results(data)
        print("Json exists, no response burned")
        

def req_rawg_data(response):
    if response.status_code != 200:
        print(f"Error: An error occured, status code: {response.status_code}, check your internet connection.")
        return
    try:
        return response.json()
    except json.JSONDecodeError:
        print("Error: Recieved bad response, cant convert to JSON")
        return None

def display_results(data):
    for game_data in data['results']:
        if not game_data['stores'] == None:
            for store in game_data['stores']:
                storeid = store['store']['id']
                if storeid in storeids:
                    if game_data['tba'] == False:
                        release = game_data.get('released', 'TBA')
                    else:
                        release = "TBA"
                    matching = available_stores(game_data['stores'])
                    game = Game(game_data['name'], release, matching, 0)
                    game.display()
                break

def available_stores(storeid):
    lst = []
    global storeids
    for store in storeid:
        if store['store']['id'] in storeids:
            lst.append(store['store']['name'])
    return lst


if __name__ == "__main__":
    main()