
# ERROR HANDLING 
# SyntaxError
try:
    print("Hello, World!")
except SyntaxError as e:
    print("SyntaxError:", e)

#TypeError
try:
    result = "5" + 10
except TypeError as e:
    print("TypeError:", e)

#NameError
try:
    print(variable)
except NameError as e:
    print("NameError:", e)

#IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError as e:
    print("IndexError:", e)

#KeyError
try:
    car = {'color': 'yellow', 'make':'BMW'}
    print(car['model'])
except KeyError as e:
    print("KeyError:", e)

#ValueError
try:
    num = int("abc")
except ValueError as e:
    print("ValueError:", e)

#AttributeError
try:
    my_str = "Hello, World!"
    print(my_str.uppercase())
except AttributeError as e:
    print("AttributeError:", e)

#IOError
try:
    with open("nonexistent_file.txt", "r") as file:
        contents = file.read()
except IOError as e:
    print("IOError:", e)

#ZeroDivisionError
try:
    result = 5 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

#ImportError
try:
    import nonexistent_module
except ImportError as e:
    print("ImportError:", e)
 

print('-------- FILE HANDLING ----------')

# FILE HANDLING

# ------------USING WITH STATETEMENT--------------

# Writing to a file using 'w' mode
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file using 'r' mode
with open("example.txt", "r") as file:
    content = file.read()
    print(content)    

# Appending to a file using 'a' mode
with open("example.txt", "a") as file:
    file.write("\nAppending new data.")

# Reading and writing to a file using 'r+' mode
with open("example.txt", "r+") as file:
    content = file.read(5)
    print(content)
    file.write("\nAdding new data with r+ mode.")

# Writing and reading to a file using 'w+' mode
with open("example.txt", "w+") as file:
    file.write("Writingggg and reading with w+ mode.")
    file.seek(0)
    content = file.read()
    print(content)

# Appending and reading from a file using 'a+' mode
with open("example.txt", "a+") as file:
    file.write("\nAppendingggg and reading with a+ mode.")
    file.seek(0)
    content = file.read()
    print(content)

# Deleting a file
import os

# Specify the file path
file_path = "exampl.txt"

# Check if the file exists
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File does not exist.")


# -------------WITH OPEN AND CLOSE---------------
 # Python code to illustrate append() mode
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()

# Python code to illustrate write() mode
file = open('geek.txt', 'w')
file.write("This will overwrite this line")
file.close()

# Python code to illustrate read() mode
file = open('geek.txt', 'r')
content = file.read()
print(content)
file.close()

# Python code to illustrate readlines() mode
file = open('geek.txt', 'r')
content = file.readlines()
print(content)
file.close()