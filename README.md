
---
# 🧾 Smart Personal Expense Tracker (CLI)


A command-line **Personal Expense Tracker** built with Python that allows users to record, view, filter, and analyze personal expenses.  
The project focuses on **clean logic, input validation, file handling, and data organization**.

## 🚀 Features

* Add new expenses with:

  * Category (custom, user-defined)
  * Amount
  * Description
  * Payment method (cash, credit or debit)
  * Date (automatic)
* Persistent storage using JSON files
* View all recorded expenses
* Filter expenses by:

  * Category
  * Payment method
  * Month
* Generate monthly reports including:

  * Total spending
  * Number of transactions
  * Average expense
  * Category breakdown (amount and percentage)
  * Payment method breakdown (amount and percentage)



## 🛠️ Technologies & Concepts Used

This project was intentionally built using **core Python concepts only**, without frameworks:

* Basic Syntax
* Variables and Data Types
* Strings
* Conditionals
* Loops
* Type Casting
* Exceptions
* Functions and Built-in Functions
* Lists, Sets, Dictionaries
* File Handling (JSON)
* Modular code organization
* Input validation and error handling


## 📁 Project Structure

```
expense-tracker/
│
├── main.py
├── expenses.json        # Stored expenses   (created automatically)
├── categories.json      # Stored categories (created automatically)
└── README.md
```


## ▶️ How to Run

1. Make sure you have **Python 3.10+** installed
2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   ```
3. Navigate to the project folder:

   ```bash
   cd expense-tracker
   ```
4. Run the program:

   ```bash
   python main.py
   ```

## 🧭 How It Works

### Adding an Expense

* The user selects or creates a category
* Enters an amount and description
* Chooses a payment method
* The expense is saved automatically with today’s date

### Filtering Expenses

Expenses can be filtered by:

* Category
* Payment method
* Month (`YYYY-MM`)

### Monthly Report

For a selected month, the program calculates:

* Total amount spent
* Number of transactions
* Average transaction value
* Percentage breakdown by category
* Percentage breakdown by payment method


## 📊 Example Monthly Report Output

```
MONTHLY SUMMARY FOR 2026-01

Total spent: $850.50
Transactions: 12
Average expense: $70.88

Category Breakdown:
- Food : $300.00 (35.29%)
- Transport : $150.50 (17.69%)
- Entertainment : $400.00 (47.02%)

Payment Method Breakdown:
- Credit : $500.00 (58.78%)
- Debit : $350.50 (41.22%)
```

## 🧠 Design Decisions

* **JSON storage** was chosen for simplicity and transparency
* **Sets** are used for categories to avoid duplicates
* The code is structured to be easily refactored into:

  * Classes
  * A database-backed version
  * A web or API-based application



## 📈 Possible Improvements

* Convert to an object-oriented design
* Add unit tests
* Add currency selection

## 📜 License

This project is licensed under the MIT License.

