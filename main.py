import json

def Welcome():
    print("Welcome in Simple Expense Assistant")

def menu():
    print("What action would you like to perform?")
    print("1. Add expenses to calculate")
    print("2. Show list of expenses")
    print("3. Remove expenses from calculate")
    print("4. Show total expenses")
    print("5. Exit")

Welcome()
expenses = {}

while True:
    menu()
    wynik = input()
    match wynik:
        case "1":
            print("Write name of your expenses to calculate")
            name = input()
            print("Write amount of your expenses to calculate")
            amount = int(input())
            expenses[name] = amount
            print(f"Dodano! {name}: {amount}")
            with open("expenses.json", "w") as file:
                json.dump(expenses, file)
        case "2":
            with (open("expenses.json", "r")) as file:
                expenses = json.load(file)
            for key, value in expenses.items():
                print(f"{key}: {value}")
        case "3":
            print("Remove expenses from calculate")
            expenses.clear()
        case "4":
            total = sum(expenses.values())
            print(f"Total: {total}")
        case "5":
            break

