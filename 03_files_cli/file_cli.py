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
def readfile():
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.strip())
            
def writefile():
    with open('sample.txt', 'w') as file:
        file.write("New file was created\n")
        user_input = input("write something")
        file.write(user_input + '\n'  ) 
         
def appendfile():
    with open('sample.txt', 'a') as file:
        user_input = input("Enter Something")
        file.write(user_input + '\n')        

while True:
    print("\n Main Menu")
    print("1: Read File")
    print("2: Write File")
    print("3: Append File")
    print("4: Exit")
    
    choice = input("Please select an Option")
    
    if choice == "1":
        readfile()
    elif choice == "2":
        writefile()
    elif choice == "3":
        appendfile()
    elif choice == "4":
        break 
    else:
        print("Invalid option. Try again.")



