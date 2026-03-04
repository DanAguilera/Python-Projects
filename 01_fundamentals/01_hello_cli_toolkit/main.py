import time



def ask_for_number(prompt, non_negative=true):
    while True:
        value = input(prompt)
        try:
            number = float(value)
            if non_negative and number < 0:
                print("Please enter a non-negative number.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

def tip_calculator():
    print("Welcome to the Tip Calculator!")
    
    bill_amount = ask_for_number("Enter the bill amount: ", non_negative=True)
    tip_percentage = ask_for_number("Enter the tip percentage: ")
    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount
    return tip_amount, total_bill



def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    weight = ask_for_number("Enter your weight in pounds: ")
    height = ask_for_number("Enter your height in inches: ")
    bmi = weight / (height ** 2) * 703  # Convert to BMI using imperial units
    
    return bmi
    

def simple_interest_calculator():
    print("Welcome to the Simple Interest Calculator!") # I = P x r x t
    principal = ask_for_number("Enter the principal amount: ")
    rate = ask_for_number("Enter the annual interest rate (in %): ")
    years = ask_for_number("Enter the time in years: ")
    interest = principal * rate * years / 100  # Convert rate to decimal
    
    return interest 

def countdown_timer():
    print("Welcome to the Countdown Timer!")
    seconds = int(ask_for_number("Enter the number of seconds for the countdown: "))
    original_seconds = seconds
    print("Starting countdown...")
    while seconds > 0:
        print(f"{seconds} seconds remaining...")
        time.sleep(1)
        seconds -= 1
    
    return original_seconds

def password_strength_checker():
    print("Welcome to the Password Strength Checker!")
    password = input("Enter a password to check its strength: ")

    strength = "Weak"
    if len(password) >= 8:
        strength = "Moderate"
    if len(password) >= 12 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        strength = "Strong"

    return strength

def pause():
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
            tip_amount, total_bill = tip_calculator()
            print(f"Tip Amount: ${tip_amount:.2f}, Total Bill: ${total_bill:.2f}")
            pause()
        elif choice == '2':
            bmi = bmi_calculator()
            print(f"Your BMI is: {bmi:.2f}")
            pause()
        elif choice == '3':
            interest = simple_interest_calculator()
            print(f"Simple Interest: ${interest:.2f}")
            pause() 
        elif choice == '4':
            seconds = countdown_timer()
            print(f"Countdown finished after {seconds} seconds.")
            pause()
        elif choice == '5':
            strength = password_strength_checker()
            print(f"Password Strength: {strength}")
            pause()
        elif choice == '0':
            print("Exiting the CLI Toolkit. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    menu_loop()
