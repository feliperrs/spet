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
    new_category = input("\n>>> ").strip().lower()
    if not new_category:
        print("Category cannot be empty!\n")
        return
    if new_category in categories:
        print("This category already exists.\n")
        return
        
    categories.add(new_category)  # add new category to "copy" set
    save_categories(categories) # send the "copy" set to save_categories()
    return new_category

def list_categories():
    categories = load_categories()
    print("Choose a category:")
    print("0 - Add new category")
    for index, category in enumerate(sorted(categories), start=1):
        print(f"{index} - {category.title()}")


def select_category():
    categories = sorted(load_categories())
    choice = int(input(">>> "))
    if choice == 0:
        selected_category = add_new_category()
    elif 1 <= choice <= len(categories):
        selected_category = categories[choice - 1]
    return selected_category

def select_amount():
    print("Enter the amount")
    amount = float(input("\n>>> "))
    return amount

def select_description():
    print("Enter a short description")
    description = input(">>> ")
    return description

def select_payment_method():
    print("Select the payment method:")
    payment_methods_list = ["cash", "credit", "debit"]
    for index, choice in enumerate(payment_methods_list, start=1):
        print(f"{index} - {choice.title()}")
    choice = int(input(">>> "))
    if 1 <= choice <= len(payment_methods_list):
        selected_payment_method = payment_methods_list[choice - 1]
    return selected_payment_method
        

def add_new_expense():
    print("\n# Adding a new expense #\n")
    list_categories()
    category = select_category()
    amount = select_amount()
    description = select_description()
    payment_method = select_payment_method()
    date = datetime.today().strftime('%Y-%m-%d')
    new_expense = {
        "date" : date,
        "category" : category,
        "amount" : amount,
        "description" : description, 
        "payment_method" : payment_method 
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