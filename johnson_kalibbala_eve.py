# -------------DICTIONARIES--------------------
# used to store data values in key value pairs
# dictionaries are ordered, changeable but do not allow duplicates

my_dict = {
    'phone': 'iphone',
    'iphone_model': 'iphone14pro',
    'year_of_release': 2022
}
print(my_dict)

# length
print(len(my_dict))
# data type
print(type(my_dict))
# accessing items
print(my_dict['phone'])
print(my_dict['iphone_model'])
print(my_dict['year_of_release'])

# modifying elements in adictionary
my_dict['phone']= "samsung"

y = my_dict.get("iphone_model")
print(y)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# Exercise one: use the values() method to return a list of all values in the dictionary

print(my_dict.values())

# Exercise two: to check if a key does exist in the dictionary

print(my_dict.get("iphone_model"))

# Exercise three: give an example how to change dictionary items, how to update 

my_dict['iphone_model'] = 'iphone14pro'
my_dict['phone'] = 'Itel'
print(my_dict)

# Updating the dictionary with new key-value pairs
my_dict.update({
    'color': 'silver',
    'price': 1299.99
})

# Exercise four: how to add dictionary items, remove dictionary items

my_dict['battery'] = '3400kW'
my_dict['screen'] = '12 inch'
print(my_dict)

# removig a key-value pair
my_dict.pop('battery')
print(my_dict)

my_dict.popitem()
print(my_dict)

del my_dict['iphone_model']
print(my_dict)

# Exercise 5: give an example on how you can loop through a dictionary, how to nest dictionaries


for key, value in my_dict.items():
    print(key, value)

for x in my_dict:
    print(x)


# how to nest dictionaries
car = {
    'make': 'Tesla',
    'model': 'Model S',
    'year': 2023,
    'specs': {
        'engine': 'Electric',
        'horsepower': 1020,
        'range': '390 miles',
        'features': {
            'autopilot': True,
            'panoramic_roof': True,
            'premium_audio': True
        }
    }
}

# Accessing nested dictionary values
print(car['make'])  
print(car['specs']['range'])   
print(car['specs']['features']['autopilot'])   


print("----------------NUMBERS-----------------------")

# integers, floats, complex 

w= 10 #int 
r=3.14 #float
s=4j #complex

print(type(w))
print(type(r))
print(type(s))

# Intengers
q= 7 
p=34567890
h=-42

print(type(q))
print(type(p))
print(type(h))

# Floats
i= 3.14 
k= 3.1415
l= -3.14

print(type(i))
print(type(k))
print(type(l))

# Complex
b= -4j 
m= 3+4j
x= 3j

print(type(b))
print(type(m))
print(type(x))

# Type conversions

w = 10 
r= 3.14 
s= 4j+2 

# coverting float to integer
v=int(r)
print(v)
print(type(v))

# coverting integer to float
u=float(w)
print(u)
print(type(u))

# converting a complex number to a float
g=float(s.real)
print(g)
print(type(g))


# converting to a complex number

print(complex(w))
print(complex(r))

print("----------------CASTING-----------------------")
# works mostly when you want to specify a a variable type 

h = int(20)
y = int(34.56)
a = int("8")

print(h)
print(type(y))
print(a)

print("----------------STRINGS-----------------------")
# strings

print('Hello World')

x = "Johnson"
y = 'Kalibbala'

print(x)
print(y)
print(type(x))

# multi line strings 
z = """
    This is 
    a multi line string
"""
print(z)


# strings as arrays
characters = "Hello"
print(characters[0])

# Exercise; use the len() function to determine the length of a string 

z = "hello world"
characters = "Hello"

print(len(z))
print(len(characters))

# Exercise; using a for loop in a string

x= 'JohnDoe'
for x in x:
    print(x)

# ----------Exercise give an exaple of slicing in strings

x= 'JohnDoe'
# Extract the last three characters
print(x[-3:]) 

# Extract every second character starting from index 1
print( x[1::2]) 

# Reverse the string
print( x[::-1]) 

print(x[0:3])
print(x[3:])

# how to modify strings

user_name = "Johnson"
user_name = user_name.upper()
print(user_name)


username= "Johnson"
print(user_name.lower())

# remove white space
my_name= "   Johnson "
print(my_name.strip())

# string concatenation
mo = "mo"
yes = "yes"

final = mo + yes
space = mo + "  " + yes

print(space)
print(final)

# -------------FORMATING STRINGS---------------
# works when one wants to combine a string to a number
# format() method


# name = f"My name is Johnson, I am {age}" 
#print(name)

age = 23
name = "My name is Johnson, I am {}" 
print(name.format(age))

year = 2023
number= 10
statement = "We are in the year {} and he was {} " 
print(statement.format(year,number))

print("----------------BOOLEAN-----------------------")
# These evaluate to True or False
print(20<10)
print('JOHNSON'=='JOHNSON')
print(20!=20)

print(bool(0))
print(True)


# Exercise use a condition to show how to use booleans

x = 15
y = 15

condition = (x > y)

if condition:
    print(bool(condition))
else:
    print(bool(condition))


