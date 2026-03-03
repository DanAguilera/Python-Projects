import time


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
    input("Press Enter to return to the main menu")

def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    weight = ask_for_number("Enter your weight in pounds: ")
    height = ask_for_number("Enter your height in inches: ")
    bmi = weight / (height ** 2) * 703  # Convert to BMI using imperial units
    print(f"Your BMI is: {bmi:.2f}")
    input("Press Enter to return to the main menu")

def simple_interest_calculator():
    print("Welcome to the Simple Interest Calculator!") # I = P x r x t
    principal = ask_for_number("Enter the principal amount: ")
    rate = ask_for_number("Enter the annual interest rate (in %): ")
    time = ask_for_number("Enter the time in years: ")
    interest = principal * rate * time / 100  # Convert rate to decimal
    print(f"Simple Interest: ${interest:.2f}")
    input("Press Enter to return to the main menu")

def countdown_timer():
    print("Welcome to the Countdown Timer!")
    seconds = int(ask_for_number("Enter the number of seconds for the countdown: "))
    print("Starting countdown...")
    while seconds > 0:
        print(f"{seconds} seconds remaining...")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
    input("Press Enter to return to the main menu")


    

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
            bmi_calculator()
        elif choice == '3':
            simple_interest_calculator()
        elif choice == '4':
            countdown_timer()
        elif choice == '5':
            print("You selected Option 5")
        elif choice == '0':
            print("Exiting the CLI Toolkit. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    menu_loop()
