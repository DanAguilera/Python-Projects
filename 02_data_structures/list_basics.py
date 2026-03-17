# exercise 1 List Manipulation


my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
new_number = 6
my_list.append(new_number)
my_list.remove(2)
my_list[2] = 20
print(my_list)  

# Exercise 2 - Looping through a list, create a list of tool names and print them in two diffferent ways

tools = ["Hammer", "Screwdriver", "Wrench", "Pliers"]
for tool in tools:
    print(tool)
for i in range(len(tools)):
    print(tools[i])

#Enumearte() and functionality: The enumerate() function in Python is a built-in tool that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object
#fruits = ['apple', 'banana', 'cherry']
#for index, fruit in enumerate(fruits):
    #print(f"Index {index}: {fruit}")

