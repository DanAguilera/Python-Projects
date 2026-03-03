def ask_for_number(prompt): 
    while True:
        value = input(prompt)
        try:
            number = float(value)
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

def tip_calculator():
    print("Welcome to the Tip Calculator!")
    bill_amount = ask_for_number("Enter the bill amount: ")
    tip_percentage = ask_for_number("Enter the tip percentage: ")
    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
    input("Press Enter to return to the main menu...")


def menu_loop():
    while True:
        print("Welcome to the CLI Toolkit!")
        print("1. Tip Calculator")
        print("2. BMI Calculator")
        print("3. Simple Interest Calculator")
        print("4. Countdown Timer")
        print("5. Password Strength Checker")
        print("0. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            tip_calculator()
        elif choice == '2':
            print("You selected Option 2")
        elif choice == '3':
            print("You selected Option 3")
        elif choice == '4':
            print("You selected Option 4")
        elif choice == '5':
            print("You selected Option 5")
        elif choice == '0':
            print("Exiting the CLI Toolkit. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    menu_loop()
