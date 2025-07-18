import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

FILE_NAME = "expenses.csv"

# Ensure CSV file exists with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Transport, Shopping, etc.): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount (₹): "))

    with open(FILE_NAME, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, amount])
    
    print("✅ Expense added successfully!\n")

def show_expenses():
    total = 0
    category_total = {}

    with open(FILE_NAME, mode='r') as f:
        reader = csv.DictReader(f)
        print("\n--- Expense Report ---")
        for row in reader:
            print(f"{row['Date']} | {row['Category']} | {row['Description']} | ₹{row['Amount']}")
            amt = float(row['Amount'])
            total += amt
            category_total[row['Category']] = category_total.get(row['Category'], 0) + amt

    print("\n💰 Total Spent: ₹", total)
    print("📊 Category-wise Breakdown:")
    for cat, amt in category_total.items():
        print(f"  {cat}: ₹{amt}")
    print()

def show_monthly_graph():
    monthly_total = defaultdict(float)

    with open(FILE_NAME, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                date_obj = datetime.strptime(row['Date'], "%Y-%m-%d")
                month_str = date_obj.strftime("%Y-%m")
                monthly_total[month_str] += float(row['Amount'])
            except:
                continue

    if not monthly_total:
        print("No data available to display chart.")
        return

    # Sort by month
    sorted_months = sorted(monthly_total.keys())
    expenses = [monthly_total[month] for month in sorted_months]

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(sorted_months, expenses, color='skyblue')
    plt.title("Monthly Expenses Overview")
    plt.xlabel("Month")
    plt.ylabel("Total Spent (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()

def menu():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Report")
        print("3. Show Monthly Expense Chart")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            show_monthly_graph()
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
 