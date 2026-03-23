with open('sample.txt', 'r') as file:
    for line in file:
        print(line)
    
with open('sample.txt', 'w') as file:
    file.write("Hello")
    file.write(input("write something?"))