# with open('sample.txt', 'a') as file:
#     user_input = input("Enter something? ")
    
#     file.write(user_input + "\n")


# with open('sample.txt', 'w') as file:
#     file.write("This file was created by Python\n")
#     user_input = input("Write something: ")
#     file.write(user_input + "\n")   
    
# with open('sample.txt', 'r') as file:
#     for line in file:
#         print(line)

# file_path = 'sample.txt'

# try:
#     with open(file_path, 'r') as file:
#         contents = file.read()
#         print("File found, Contents:")
#         print(contents)
    
# except FileNotFoundError:
#     print(f"File not found: {file_path}. Creating File")
#     with open(file_path, 'w') as file:
#         file.write("created a file")
#     print(f"File '{file_path}' created")
    
# with open(file_path, 'r') as file:
#     contents = file.read()
#     print("\n Reading file")
#     print(contents)
from datetime import datetime

datetime.now()

filename = input("Enter file name: ")

#OPTION 1
def readfile():
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File does not exist yet")
        
#OPTION 2            
def writefile():
    with open(filename, 'w') as file:
        file.write("New file was created\n")
        user_input = input("write something? ")
        file.write(user_input + '\n'  ) 

#OPTION 3     
def appendfile():
    with open(filename, 'a') as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_input = input("Enter Something: ")
        file.write(f"[{current_time}] {user_input}\n")

#OPTION 4       
def searchfile():
    keyword = input("Enter a keyword to search for: ").lower()
    found = False

    try:
        with open(filename, 'r') as file:
            for index, line in enumerate(file, start=1):
                if keyword in line.lower():
                    print(f"Line {index}: {line.strip()}")
                    found = True

        if not found:
            print("No matches found.")

    except FileNotFoundError:
        print("File does not exist yet.")
  


def menuloop():
    while True:
        print("\n Main Menu")
        print("1: Read File")
        print("2: Write File")
        print("3: Append File")
        print("4: Search File")
        print("5: Exit")
    
        choice = input("Please select an Option? ")
    
        if choice == "1":
            readfile()
        elif choice == "2":
            writefile()
        elif choice == "3":
            appendfile()
        elif choice == "4":
            searchfile()
        elif choice == "5":
            break
        else:
            print("Choose a valid option")
            
            
menuloop()