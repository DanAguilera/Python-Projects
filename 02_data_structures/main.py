import math 
import numbers
import time

def tip_calculator():
    bill_amount = float(input("Enter the bill amount: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    
    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount
    
    return tip_amount, total_bill

def bmi_calculator():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    
    bmi = weight / (height ** 2) * 703  # Convert to BMI using imperial units
    
    return bmi

def simple_interest_calculator():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    years = float(input("Enter the time in years: "))
    
    interest = principal * rate * years / 100  # Convert rate to decimal
    
    return interest 

def countdown_timer():      
    seconds = int(input("Enter the number of seconds for the countdown: "))
    original_seconds = seconds
    print("Starting countdown...")
    while seconds > 0:
        print(f"{seconds} seconds remaining...")
        time.sleep(1)
        seconds -= 1
    
    return original_seconds

def password_strength_checker():
    password = input("Enter a password to check its strength: ")
    
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(not char.isalnum() for char in password)
    
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    if strength_score == 5:
        return "Strong"
    elif strength_score >= 3:
        return "Moderate"
    else:
        return "Weak"

def pause():
    input("Press Enter to return to the main menu")     

menu = {
    "1": ("Tip Calculator", tip_calculator),
    "2": ("BMI Calculator", bmi_calculator),
    "3": ("Simple Interest Calculator", simple_interest_calculator),
    "4": ("Countdown Timer", countdown_timer),
    "5": ("Password Strength Checker", password_strength_checker),
    "6": ("Exit", None)
}

def menu_loop():
    while True:
        print("\nWelcome to the CLI Toolkit!")
        for key, (name, _) in menu.items():
            print(f"{key}. {name}")
        
        choice = input("Please select an option: ")
        
        if choice in menu:
            if choice == "6":
                print("Exiting the CLI Toolkit. Goodbye!")
                break
            
            _, func = menu[choice]
            result = func()
            print(f"Result: {result}")
            pause()
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    menu_loop()
    
