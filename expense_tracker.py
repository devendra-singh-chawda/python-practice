while True:

    print("\nExpense Tracker ")

    print("1. Add Expense")

    print("2. View Expenses")

    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        item = input("Enter expense name: ")

        amount = input("Enter amount: ")

        file = open("expenses.txt", "a")

        file.write(item + " - " + amount + "\n")

        file.close()

        print("Expense added successfully!")

    elif choice == "2":

        file = open("expenses.txt", "r")

        data = file.read()

        print("\nExpenses:\n")

        print(data)

        file.close()

    elif choice == "3":

        print("Exiting program...")

        break

    else:

        print("Invalid choice")