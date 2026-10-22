from sys import exit, stdout
import re
import os
import time

lst = [1,2]

def main():
    while True:
        clear()
        menu()
        try:
            choice = int(input(f"What is your choice (1, 2) ? "))
            if choice not in lst:
                raise ValueError
        except ValueError:
            print("Invalid Value")
            time.sleep(2)
            continue
        match int(choice):
            case 1:
                query = input("Title: ").strip()
                ...
            case 2:
                print("Goodbye!")
                time.sleep(1)
                break
    clear()


def clear():
    # 'nt' means Windows, 'posix' means Mac or Linux
    os.system('cls' if os.name == 'nt' else 'clear')



def menu():
    print(f"""
1. Search for a game
2. Exit
    """)
        
        
    

if __name__ == "__main__":
    main()