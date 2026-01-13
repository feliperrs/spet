import json


def main_menu():
    print("\nWhat do you want to do ?")
    print("1 - Add a new expense")
    print("2 - View all expenses")
    print("3 - Filter expenses")
    print("4 - Monthly report")
    print("0 - Exit")
    choice = int(input('\n>>> '))
    return choice



def add_new_expense():
    pass

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