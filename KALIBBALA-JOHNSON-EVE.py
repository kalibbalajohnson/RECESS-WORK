print('------------Exercise1-------------------')
names = ["John", "Peter", "Jane", "Paul", "Mary"]
print(names[1])

# change the value of the first item to  a new value
names[0] = "Mary"

# add a sixt name to the list
names.append("George")
print(names)

# add "Bathel" as the third item in your list
names.insert(2, "Bathel")
print(names)

# remove the fourth item from the list
names.pop(3)
print(names)

# use negative indexing to print the last item in the list
print(names[-1])

# create a new list with 7 items and use a range of indexes to print the third fourth and fifth items
user_names = ["John", "Peter", "Jane", "Paul", "Mary", "George", "Bathel"]
print(user_names[2:5])

#write a list of countries and make a copy of it
countries = ["France", "Germany", "Italy", "Spain", "Switzerland"]
countries_copy = countries.copy()
print(countries)
print(countries_copy)

# write a program to loop through the list of countries
countries = ["France", "Germany", "Italy", "Spain", "Switzerland"]
for country in countries:
    print(country)

#write a list of animal names and sort them in both descending and ascending order
animals = ["dog", "cat", "bird", "fish", "cow", "horse", "pig"]
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)

# using the list above, write a python program to ouput only animal names with the letter 'a' in them
animals = ["dog", "cat", "bird", "fish", "cow", "horse", "pig"]
for animal in animals:
    if "a" in animal:
        print(animal)

# write two lists, one containing first names and the other with second names, join the two lists
first_names = ["John", "Peter", "Jane", "Paul", "Mary", "George", "Bathel"]
second_names = ["Dorothy", "Malik", "Oyella", "Doe", "Mike", "Hose", "Male"]
names = first_names + second_names
print(names)

print('------------Exercise2-------------------')

# print a brand
x =("samsung", "iphone", "tecno","redmi")
print(x[1])

#use negative indexing to print the second last item in the tuple
print(x[-2])

# using the phones list above, write a program to update "iphone" to "itel"
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)

# add "Huawei" to the turple
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)  
x_list.append("Huawei")
x = tuple(x_list)  
print(x)


# loop through the tuple
for phone in x:
    print(phone)

# remove /delete the first item from the tuple
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)  
x_list.pop(0)  
x = tuple(x_list)  
print(x)

# using the tuple constructor, create a tuple of 5 cities in Uganda
cities = tuple(('Kampala', 'Entebbe', 'Jinja', 'Gulu', 'Mbale'))

# write a program to un pack the tuple 
cities = tuple(('Kampala', 'Entebbe', 'Jinja', 'Gulu', 'Mbale'))
city1, city2, city3, city4, city5 = cities

print(city1)
print(city2)
print(city3)
print(city4)
print(city5)

# Print the 2nd, 3rd, and 4th cities
print(cities[1:4])


# write two tuples , one containing first names and the other second names and join the two tuples 

first_names = ('John', 'Peter', 'Jane', 'Paul', 'Mary')
second_names = ('Kalibbala', 'Musa', 'Doyella', 'Heaton', 'Murungi')

full_names = first_names + second_names
print(full_names)

# create a tuple of colors and multiply it by 3

colors = ('pink', 'blue', 'green', 'yellow', 'black')
print(colors * 3)

# return the number of times 8 appears in this tuple 
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)

print(count_8)

print('------------Exercise3-------------------')

 # 1
beverages = set(["vodka", "tea", "juice"])
print(beverages)

# 2

beverages.add('bushera')
beverages.add('soda')
print(beverages)

# 3
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")

# 4
mySet = {"oven", "kettle", "microwave", "refrigerator"}

mySet.remove("kettle")

print(mySet)


# 5

for item in mySet:
    print(item)

# 6 
mySet = {"jackfruit", "peach", "apricot", "grape"}
myList = ["mango", "kiwi"]

mySet.update(myList)

print(mySet)

# 7
ages = {25, 30, 35, 40}
first_names = {"John", "Peter", "Jane", "Paul"}

# Join the two sets
joined_set = ages.union(first_names)

print(joined_set)

print('------------Exercise4-------------------')

# 1 
number = 10
text = " years old"

concatenated = str(number) + text
print(concatenated)

# 2 
txt = " Hello, Uganda! "

# Remove spaces at the beginning and end
trimmed = txt.strip()
print(trimmed)

# 3
txt = "Hello, Uganda!"

uppercase_txt = txt.upper()
print(uppercase_txt)

# 4
txt = "Hello, Uganda!"

modified_txt = txt.replace('U', 'V')
print(modified_txt)

# 5
y = "I am proudly Ugandan"

substring = y[1:4]
print(substring)

# 6
x = 'All "Data Scientists" are cool!'
print(x)

print('------------Exercise5-------------------')

# 1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

shoe_size = Shoes["size"]
print(shoe_size)

# 2
Shoes["brand"] = "Adidas"
print(Shoes)

# 3
Shoes["type"] = "sneakers"

# 4
print(Shoes.keys())

# 5
print(Shoes.values())

# 6
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")

# 7
for key, value in Shoes.items():
    print(key, ":", value)

# 8 
del Shoes["color"]
print(Shoes)

# 9
Shoes.clear()

# 10
original_dict = {
    "name": "Johnson",
    "height": 25,
    "gender": "male"
}

copy_dict = original_dict.copy()

copy_dict["height"] = 30

print(original_dict)
print(copy_dict)

# 11
# nested dictionary
company = {
    "name": "ABC Corporation",
    "departments": {
        "sales": {
            "manager": "John Smith",
            "employees": {
                "employee1": {
                    "name": "Alice Johnson",
                    "position": "Sales Representative"
                },
                "employee2": {
                    "name": "Bob Anderson",
                    "position": "Sales Executive"
                }
            }
        },
        "marketing": {
            "manager": "Jane Doe",
            "employees": {
                "employee1": {
                    "name": "Eve Roberts",
                    "position": "Marketing Specialist"
                },
                "employee2": {
                    "name": "Frank Williams",
                    "position": "Marketing Coordinator"
                }
            }
        }
    }
}

# Creating a nested dictionary for a football team
team = {
    "name": "Real Madrid",
    "country": "Spain",
    "stadium": "Santiago Bernabeu",
    "captain": "Sergio Ramos",
    "top_scorer": "Cristiano Ronaldo",
    "titles": {
        "La Liga": 34,
        "UEFA Champions League": 13,
        "Copa del Rey": 19
    }
}

# Accessing values in the nested dictionary
print("Team Name:", team["name"])
print("Top Scorer:", team["top_scorer"])

print( team["titles"]["La Liga"])
print(team["titles"]["UEFA Champions League"])

# updating values in the nested dictionary
team["captain"] = "Karim Benzema"
team["titles"]["La Liga"] = 35
team["titles"]["Copa del Rey"] = 20

# adding a new 
team["titles"]["Super Cup"] = 3
team["manager"] = "Carlo Ancelotti"

# deleting 
del team["titles"]["La Liga"]

# Get all values in the nested dictionary ("titles")
nested_values = team["titles"].values()
print(nested_values)

# Get all keys in the nested dictionary ("titles")
nested_keys = team["titles"].keys()
print(nested_keys)

# Loop through the inner dictionary
for title, count in team["titles"].items():
    print(f"{title}: {count}")

# Update the "titles" dictionary with new key-value pairs
new_titles = {
    "Super Cup": 4,
    "FIFA Club World Cup": 4
}
team["titles"].update(new_titles)    
print(team["titles"])
 

