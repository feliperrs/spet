import json
from datetime import datetime
import os

cls = lambda: os.system('cls') # cleans console


def main_menu():
    print("What do you want to do ?")
    print("1 - Add a new expense")
    print("2 - View all expenses")
    print("3 - Filter expenses")
    print("4 - Monthly report")
    print("0 - Exit")
    choice = int(input('\n>>> '))
    return choice

# -------------------------------- CATEGORIES -------------------------------- #

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
            "categories.json exists but contains invalid JSON."
        )

def save_categories(categories: set):   # receive a set from add_new_category()
    with open("categories.json", "w") as file:
        json.dump(sorted(categories), file, indent=2) # save the set as a sorted list

def add_new_category():
    while True:
        categories = load_categories()
        
        print("Type the new category:")
        new_category = input("\n>>> ").strip().lower()
        if not new_category:
            print("Category cannot be empty!\n")
            continue
        if new_category in categories:
            print("This category already exists.\n")
            return new_category
        
        print(f"\nNew category '{new_category.title()}' added")   
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
    while True:
        categories = sorted(load_categories())
        try:
            list_categories()
            choice = int(input("\n>>> "))
        except ValueError:
            cls()
            print(f"Select a NUMBER from 0 to {len(categories)}\n")
            continue
        else:
            if choice == 0:
                selected_category = add_new_category()
            elif 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
            else:
                cls()
                print(f"Select from 0 to {len(categories)}\n")
                continue
        return selected_category

# ---------------------------------- AMOUNT ---------------------------------- #

def select_amount():
    cls()
    while True:
        print("Enter the amount")
        try:
            amount = float(input("\n>>> "))
        except ValueError:
            cls()
            print("Insert a number\n")
            continue
        return amount

# -------------------------------- DESCRIPTION ------------------------------- #

def select_description():
    cls()
    while True:
        print("Enter a short description")
        description = input("\n>>> ")
        if not description:
            cls()
            print("You must enter a short description\n")
            continue
        return description

# ------------------------------ PAYMENT METHOD ------------------------------ #

def select_payment_method():
    cls()
    while True:
        print("Select the payment method:")
        payment_methods_list = ["cash", "credit", "debit"]
        for index, choice in enumerate(payment_methods_list, start=1):
            print(f"{index} - {choice.title()}")
        try:
            choice = int(input("\n>>> "))
        except ValueError:
            cls()
            print(f"You must enter a NUMBER from 1 to {len(payment_methods_list)}\n")
            continue
        else:
            if 1 <= choice <= len(payment_methods_list):
                selected_payment_method = payment_methods_list[choice - 1]
            else:
                cls()
                print(f"Select an option from 1 to {len(payment_methods_list)}\n")
                continue
        return selected_payment_method
        
# ---------------------------------- EXPENSE --------------------------------- #

def load_expenses():
    try:
        with open ("expenses.json", "r") as file:
            return list(json.load(file))
    except FileNotFoundError:
        with open ("expenses.json", "w") as file:
            json.dump([], file)
            return list()
    except json.decoder.JSONDecodeError:
        raise ValueError(
            "expenses.json exists but contains invalid JSON."
        )
    
def save_new_expense(expense):
    expenses = load_expenses()
    expenses.append(expense) 
    with open ("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)    
    
    
def add_new_expense():
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
    save_new_expense(new_expense)
    cls()
    print("# Adding a new expense #")
    print("\nYour expense was added !")
    print(f"Description: {new_expense['description'].capitalize()}")
    print(f"Amount: ${new_expense['amount']:.2f}")
    print(f"Category: {new_expense['category'].title()}")
    print(f"Payment Method: {new_expense['payment_method'].title()}")

# ------------------------------- VIEW EXPENSES ------------------------------ #

def view_all_expenses():
    expenses_list = load_expenses()
    cls()
    print("List of Expenses:\n")
    for expense in expenses_list:
        print(f"Description: {expense['description']}")
        print(f"Amount: ${expense['amount']:.2f}")
        print(f"Category: {expense['category'].capitalize()}")
        print(f"Payment Method: {expense['payment_method'].title()}")
        print(f"Date: {expense['date']}\n")

# ----------------------------- FILTER EXPENESES ----------------------------- #

def list_filter_categories():
    categories = load_categories()
    print("Choose a category:")
    for index, category in enumerate(sorted(categories), start=1):
        print(f"{index} - {category.title()}")

def select_filter_categories():
    while True:
        categories = sorted(load_categories())
        try:
            choice = int(input("\n>>> "))
        except ValueError:
            cls()
            print(f"\nSelect a NUMBER from 0 to {len(categories)}\n")
            continue
        else:
            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
            else:
                cls()
                print(f"\nSelect from 1 to {len(categories)}\n")
                continue
        return selected_category

def filter_by_category():
    cls()
    list_filter_categories()
    category = select_filter_categories()
    expenses_list = load_expenses()
    cls()
    for expense in expenses_list:
        if category == expense["category"]:
            print(f"\nDescription: {expense['description'].capitalize()}")
            print(f"Amount: ${expense['amount']:.2f}")
            print(f"Category: {expense['category'].title()}")
            print(f"Payment Method: {expense['payment_method'].title()}")
            print(f"Date: {expense['date']}\n")

def filter_by_payment_method():
    selected_payment_method = select_payment_method()
    expenses_list = load_expenses()
    for payment in expenses_list:
        if selected_payment_method == payment["payment_method"]:
            print(f"\nDescription: {payment['description'].capitalize()}")
            print(f"Amount: ${payment['amount']:.2f}")
            print(f"Category: {payment['category'].title()}")
            print(f"Payment Method: {payment['payment_method'].title()}")
            print(f"Date: {payment['date']}\n")

def filter_by_date():
    cls()
    while True:
        expenses_list = load_expenses()
        date_list = []
        for expense in expenses_list:
            if expense['date'][:7] not in date_list:
                date_list.append(expense['date'][:7])
        print("Select a MONTH to filter:")
        for index, month in enumerate(date_list, start=1):
            print(f"{index} - {month}")
        try:
            month_choice = int(input("\n>>> "))
        except ValueError:
            cls()
            print(f"Select a NUMBER from 1 to {len(date_list)}\n")
            continue
        if 1 <= month_choice <= len(date_list):
            selected_month = date_list[month_choice - 1]
            for expense in expenses_list:
                if expense['date'][:7] == selected_month:
                    print(f"\nDescription: {expense['description'].capitalize()}")
                    print(f"Amount: ${expense['amount']:.2f}")
                    print(f"Category: {expense['category'].title()}")
                    print(f"Payment Method: {expense['payment_method'].title()}")
                    print(f"Date: {expense['date']}\n")
        else:
            cls()
            print(f"Select from 1 to {len(date_list)}\n")
            continue
    
    
def filter_expenses():
    while True:
        print("How do you want to filter?\n")
        print("1 - By CATEGORY")
        print("2 - By PAYMENT METHOD")
        print("3 - By DATE")
        print("0 - BACK")
        try:
            user_choice = int(input("\n>>> "))
        except ValueError:
            cls()
            print("Select a NUMBER from 1 to 3\n")
            continue
        if user_choice == 1:
            filter_by_category()
        elif user_choice == 2:
            filter_by_payment_method()
        elif user_choice == 3:
            filter_by_date()
        elif user_choice == 0:
            cls()
            break
        else:
            cls()
            print("Select from 1 to 3\n")
    
# ---------------------------------- REPORT ---------------------------------- #

def select_month_report():
    cls()
    while True:
        expenses_list = load_expenses()
        date_list = []
        for expense in expenses_list:
            if expense['date'][:7] not in date_list:
                date_list.append(expense['date'][:7])
        print("Select a MONTH to check the report:")
        for index, month in enumerate(date_list, start=1):
            print(f"{index} - {month}")
        try:
            month_choice = int(input("\n>>> "))
        except ValueError:
            cls()
            print(f"Select a NUMBER from 1 to {len(date_list)}\n")
            continue
        if 1 <= month_choice <= len(date_list):
            selected_month = date_list[month_choice - 1]
        else:
            cls()
            print(f"Select from 1 to {len(date_list)}\n")
            continue
        return selected_month

def monthly_report_summary(selected_month):
    cls()
    print(f"MONTHLY SUMMARY FOR {selected_month}\n")
    expenses_list = load_expenses()
    total_spent = 0
    total_transactions = 0
    for expense in expenses_list:
        if expense['date'][:7] == selected_month:
            total_spent += expense['amount']
            total_transactions += 1
    average_expense = total_spent / total_transactions
    
    print(f"Total spent: ${total_spent}")
    print(f"Transactions: {total_transactions}")
    print(f"Average expense: ${average_expense}")

def category_breakdown(selected_month):
    expenses_list = load_expenses()
    
    total_spent = 0
    category_totals = {}
    
    for expense in expenses_list:
        if expense['date'][:7] == selected_month:
            total_spent += expense['amount']
            category = expense['category']
            amount = expense['amount']
            if expense['category'] not in category_totals:
                    category_totals[category] = 0
            category_totals[category] += amount
            
    print("\nCategory Breakdown:")
    category_percentages = {}
    for category, amount in category_totals.items():
        percentage = (amount / total_spent) * 100
        category_percentages[category] = percentage
    
    for category in category_totals:
        amount = category_totals[category]
        percentage = category_percentages[category]
        print(f"- {category.title()} : ${amount:.2f} ({percentage:.2f}%)")
    
    
def payment_method_breakdown(selected_month):
    expenses_list = load_expenses()
    
    total_spent = 0
    paymenth_method_totals = {}
    
    for expense in expenses_list:
        if expense['date'][:7]== selected_month:
            total_spent += expense['amount']
            payment_method = expense['payment_method']
            amount = expense['amount']
            if expense['payment_method'] not in paymenth_method_totals:
                paymenth_method_totals[payment_method] = 0
            paymenth_method_totals[payment_method] += amount
    
    print(f"\nPayment Method Breakdown:")
    payment_method_percentages = {}
    for method, amount in paymenth_method_totals.items():
        percentage = (amount / total_spent) * 100
        payment_method_percentages[method] = percentage
    
    for method in paymenth_method_totals:
        amount = paymenth_method_totals[method]
        percentage = payment_method_percentages[method]
        print(f"- {method.title()} : ${amount:.2f} ({percentage:.2f}%)")
        
        
def monthly_report():
    selected_month = select_month_report()
    monthly_report_summary(selected_month)
    category_breakdown(selected_month)
    payment_method_breakdown(selected_month)
    print("\n")

# ----------------------------------- MAIN ----------------------------------- #

while True:
    try:
        user_choice = main_menu()
        cls()
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