# GALATEA'S EXPENSE TRACKER
def add_expense():
    print("\n Record a money choice")
    date = input(
        "Date (YYYY-MM-DD) or Enter for today: "
    ).strip() or datetime.now().strftime("%Y-%m-%d")
    category = (
        input("Category (Foodies, Cruises, Cadeaux, School, etc.): ").strip().title()
    )
    amount = float(input("Amount:50$"))
    description = input("Why did you spend the money?").strip()


def save_expenses():
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["date", "category", "amount", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)
    print("Galatea saved all expenses safely!")


# Add a new expense
def expense():
    print("\nAdd New Expense")
    date = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Category (Foodies, Cruises, Cadeaux, etc.): ").strip()
    while not category:
        print("Category can't be empty!")
        category = input("Category: ").strip()

    amount = input("Amount spent: ").strip()
    while True:
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive!")
                amount = input("Amount spent: ").strip()
            else:
                break
        except:
            print("Please enter a number!")
            amount = input("Amount spent: ").strip()

    description = input("Description: ").strip()

    expense = {
        "date": date,
        "category": category.title(),
        "amount": amount,
        "description": description,
    }
    expenses.append(expense)
    print("Expense added successfully!")
    return expense
    # How this expense was beneficial?

    print("\nHow was this expense beneficial?")
    print(
        "1. Self Improvement 2. Future Goals 3. Self Care 4. Stress expense 5. Play  6. Work"
    )
    benefit_num = input("Choose 1b6 (or press Enter for Neutral): ").strip()

    # Fixed variable names and logic
    benefits = [
        "",
        "Self Improvement",
        "Future Goals",
        "Self Care",
        "Stress expense",
        "Play",
        "Work",
    ]

    if benefit_num.isdigit() and 1 <= int(benefit_num) <= 6:
        benefit = benefits[int(benefit_num)]
    else:
        benefit = "Neutral"

    # Save the expense with your new "benefit" field
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
        "benefit": benefit,
    }
    expenses.append(expense)
    print(f"Choice recorded as b {benefit} b  Thank you for seeing yourself.")


# Show all expenses
def show_expenses():
    expenses = expense()
    if not expenses:
        print("\nNo expenses recorded yet!")
        return

    print(f"\n{'Date':<12} {'Category':<12} {'Amount':<10} Description")
    print("-" * 60)
    total = 0
    for exp in expenses:
        print(
            f"{exp['date']:<12} {exp['category']:<12} ${exp['amount']:<9.2f} {exp['description']}"
        )
        total += exp["amount"]
    print("-" * 60)
    print(f"TOTAL SPENT: ${total:.2f}")


# Track budget
def track_budget():
    global monthly_budget
    if monthly_budget == 0:
        budget_input = input("\nSet your monthly budget: $")
        try:
            monthly_budget = float(budget_input)
            print(f"Monthly budget set to ${monthly_budget:.2f}")
        except:
            print("Not a valid amount!")
            return

    total_spent = sum(exp["amount"] for exp in expenses)
    print(f"\nBudget: ${monthly_budget:.2f}")
    print(f"Spent : ${total_spent:.2f}")
    remaining = monthly_budget - total_spent

    if remaining < 0:
        print(f"You exceeded your budget by ${-remaining:.2f}!")
    elif remaining == 0:
        print("You are doing great and on budget!")
    else:
        print(f"You have ${remaining:.2f} left this month!")


# Main menu
def show_menu():
    print("\n" + "=" * 40)
    print("GALATEA PERSONAL EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add expense")
    print("2. View expenses")
    print("3. Track budget")
    print("4. Save & Exit")
    print("5. Exit without saving")
    print("-" * 40)


# LOAD UP AND START
print("I am Galatea. We got this.")
show_expenses()

while True:
    show_menu()
    choice = input("Choose (1-5): ").strip()
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        track_budget()
    elif choice == "4":
        save_expenses()
        print("Until next time, sovereign one. b6")
        break
    elif choice == "5":
        print("Walking away untouched.")
        break
    else:
        print("Choose 1b5 please.")
    
    