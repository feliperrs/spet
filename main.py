import json
from datetime import datetime


def main_menu():
    print("\nWhat do you want to do ?")
    print("1 - Add a new expense")
    print("2 - View all expenses")
    print("3 - Filter expenses")
    print("4 - Monthly report")
    print("0 - Exit")
    choice = int(input('\n>>> '))
    return choice


def load_categories():
    try:
        with open("categories.json", "r") as file:
            return set(json.load(file)) # return saved list as a set
    except FileNotFoundError:
        with open("categories.json", "w") as file:
            json.dump([], file) # creates a new categories.json with empty list
        return set()    # return an empty set if there is no categories.json
    except json.decoder.JSONDecodeError:
        raise ValueError(
            "categories.json exists but contains invalid JSON. "
        )

def save_categories(categories: set):   # receive a set from add_new_category()
    with open("categories.json", "w") as file:
        json.dump(sorted(categories), file, indent=2) # save the set as a sorted list

def add_new_category():
    categories = load_categories()
    
    print("Type the new category:")
    new_category = input(">>> ").strip().lower()

    if not new_category:
        print("Category cannot be empty!\n")
        return
    if new_category in categories:
        print("This category already exists.\n")
        return
    
    categories.add(new_category)  # add new category to "copy" set
    save_categories(categories) # send the "copy" set to save_categories()
    


def add_new_expense():
    print("# Adding a new expense #")
    print("Choose a category:")
    print("CATEGORY LIST")
    print("0 - Add new category")
    choice = int(input(">>> "))
    if choice == 0:
        add_new_category()
    date = datetime.today().strftime('%Y-%m-%d')
    new_expense = {
        "date" : date
    }
    print(new_expense)

def view_all_expenses():
    pass

def filter_expenses():
    pass

def monthly_report():
    pass

while True:
    try:
        user_choice = main_menu()
    except ValueError:
        print("\nYou should enter a number !\n")
    else:
        if user_choice == 1:
            add_new_expense()
        elif user_choice == 2:
            view_all_expenses()
        elif user_choice == 3:
            filter_expenses()
        elif user_choice == 4:
            monthly_report()
        elif user_choice == 0:
            break            
        else:
            print("\nYou should enter a number from 1 to 4 !\n")