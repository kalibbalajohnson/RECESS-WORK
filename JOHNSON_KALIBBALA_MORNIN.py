# day 3
# Basic  operators and expresions (input and out put operators)

'''
Arithmetic Operators
+ Addition
- Sabtraction
* Multiplication
/ Division
// divide and return answer without remainder
% Modulus
** Exponential

Comparison operators
== Equal to
!= Not Equal !==
> Greater than
< Less than 
>= Greater than or equal to
<= Less than or equal to

Logical Operators
Logical AND 'and'
Logical OR 'or'
Logical NOT 'not'

Assignment Operators
Assign value: '='
Add value: '+'
Add and assign value: '+='
Multiply and assign value: '*='
Divide and assign value: '/='
Modulus and assign value: '%='
Exponentiate and assign value: '**='

Membership Operators:
In: 'in' operator: checks if a value exists in a sequence
Not in: 'not in' operator: checks if two values are the same
Is not: 'is not' operator: checks if two values are not the same

'''
# Examples of arithmetic operators
#+ Addition


a = 30 + 20
print(a)
#- Sabtraction
a = 30 - 20
print(a)
# * Multiplication
a = 30 * 20
print(a)
# / Division
a = 30 / 20
print(a)
# // divide and return answer without remainder
a = 30 // 20
print(a)
# % Modulus
a = 30 % 20
print(a)
# ** Exponential
a = 30 ** 4
print(a)


# Comparison operators
x = 2
y = 4

# Greater than
if x > y:
    print('a is greater than')
    print(x > y)

# Less than
if x < y:
    print('a is greater than')
    print(x < y)

# Greater than or equal to
if x >= y:
    print('a is greater than')
    print(x >= y)

# Less than or equal to
if x <= y:
    print('a is greater than')
    print(x <= y)

# Equal to
if x == y:
    print('a is greater than')
    print(x == y)
# Equal to
if x == y:
    print('a is greater than')
    print(x > y)

# Equal to
if x != y:
    print('a is greater than')
    print(x != y)


# Examples with Logical operators
# Logical operators
a = True
b = False

# Logical AND
print(a and b)

# Logical OR
print(a or b)

# Logical NOT
print(not a)
print(not b)

# Logical AND
print(a and b)

# Assignment Operators
# Compound assignment operators

a = 5
b = 21
c = 7
d = 3
e = 4
f = 10

# Add and assign
a += 5
print(a)

# Subtract and assign
b -= 5
print(b)

# Multiply and assign
c *= 5
print(c)

# Divide and assign
d /= 5
print(d)

# Modulus and assign
e %= 5
print(e)

# Exponentiation and assign
f **= 5
print(f)

# Membership assignment operators
cars = ['jeep', 'tesla', 'BMW', 'RollsRoyce']

if 'jeep' in cars:
    print('jeep is in the list')
    print('tesla' in cars)
    print('toyota' in cars)

# Identity Operators
x = 10
y = 10

# is operator
print(x is y)
print(x is not y)
print(x == y)
print(x != y)
print(x < y)
print(x <= y)

# List
z = [1, 2, 3, 4, 5, 6, 7]
w = [1, 2, 3, 4, 5, 6, 7]
print(z is not w)

# Bitwise Operators
'''
They are used to perform operations on individual bits in of binary numbers
Bitwise AND ('&'): Performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR ('|'): Performs a bitwise OR operation between the corresponding bits of two integers
Bitwise XOR ('^'): Performs a bitwise XOR operation between the corresponding bits of two integers
Bitwise NOT ('~'): Performs a bitwise NOT operation between the corresponding bits of two integers
Bitwise left shift ('<<'): Performs a bitwise left shift operation between the corresponding bits of two integers
Bitwise right shift ('>>'): Performs a bitwise right shift operation between the corresponding bits of two integers
'''

# Examples of Bitwise Operations
a = 10
b = 20

result = a & b
print(result)

result = a | b
print(result)

result = a ^ b
print(result)

result = ~a
print(result)

result = a << 2
print(result)

result = a >> 2
print(result)


# Exercise1 create a simple calculator with a GUI interface to (add, sub, mult, divide)
# make the title of calculator program window with your name e.g Johnson Kalibbala simple calculator
# use tkinter learn

import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Kalibbala Johnson")  # Replace "Your Name" with your actual name

# Function to perform the calculation
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operator = operator_var.get()

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operator"

    result_label.config(text="Result: " + str(result))


# Create entry fields
label1 = tk.Label(window, text="Entry 1:", font=("Arial", 10))
label1.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

entry1 = tk.Entry(window, width=11, font=("Arial", 12))
entry1.grid(row=0, column=1, padx=10, pady=5)

# Existing code...

label2 = tk.Label(window, text="Entry 2:", font=("Arial", 10))
label2.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

entry2 = tk.Entry(window, width=11, font=("Arial", 12))
entry2.grid(row=1, column=1, padx=10, pady=5)

# Create operator buttons
operator_var = tk.StringVar(window)

operator_frame = tk.Frame(window)
operator_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

button_plus = tk.Button(operator_frame, text="+", width=5, command=lambda: operator_var.set("+"), bg="lemon chiffon")
button_plus.grid(row=0, column=0, padx=3)

button_minus = tk.Button(operator_frame, text="-", width=5, command=lambda: operator_var.set("-"), bg="lemon chiffon")
button_minus.grid(row=0, column=1, padx=3)

button_multiply = tk.Button(operator_frame, text="*", width=5, command=lambda: operator_var.set("*"), bg="lemon chiffon")
button_multiply.grid(row=0, column=2, padx=3)

button_divide = tk.Button(operator_frame, text="/", width=5, command=lambda: operator_var.set("/"), bg="lemon chiffon")
button_divide.grid(row=0, column=3, padx=3)

# Create result label
result_label = tk.Label(window, text="Result:", font=("Arial", 10, "bold"))
result_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10, columnspan=2)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate, bg="lemon chiffon")
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# Set window size and center it on the screen
window.geometry("350x250")


# Start the Tkinter event loop
window.mainloop()
