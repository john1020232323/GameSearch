from sys import exit, stdout
import re
import os
import time
import helper
import rawg_search
import cheapshark_search

lst = [1,2, 3]
methods = {
    1: rawg_search.search,
    2: cheapshark_search.search,
}

def main():
    while True:
        clear()
        menu()
        try:
            choice = int(input(f"What is your choice (1 - 3)? "))
            if choice not in lst:
                raise ValueError
            if choice == 3:
                print("Thank you!")
                time.sleep(2)
                break
            helper.handle_search(methods[choice])
        except ValueError:
            print("Invalid Value")
            time.sleep(2)
            continue
    clear()


def clear():
    # 'nt' means Windows, 'posix' means Mac or Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(f"""
1. Search for a game
2. Search for deals
3. Exit
    """)
        
        
    

if __name__ == "__main__":
    main()