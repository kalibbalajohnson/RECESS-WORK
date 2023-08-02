#store items in a single variable
#Turples are ordered and unchangable
phones=("samsung", "iphone", "Techno")
print(phones)


# duplication of values
phones=("samsung", "iphone", "Techno", "Techno", "samsung")
print(phones)

#Exercise 
#Use the len() with example
#Tuple showing different data types
#how to access tuples

#--------------------Exercise----------------------------
teams = ("manu", "arsenal", "chelsea")

print(len(teams))

print(teams[0])
print(teams[-2])
print(teams[2])
print(teams[0:3])
print(teams[1:])
print(teams[:2])
print(teams)

tuple_mixed = ("Johnson", 21, 3.14, False)

print(tuple_mixed)
print(len(tuple_mixed))

#----------------------------------------------------------


Tuple1=("matooke", "rice")
Tuple2=(100, 200, 300, 500)
print(type(Tuple2))

#add items to tuples
phones=("samsung", "iphone", "Techno")
z= list(phones)
z.append("Nokia")
phones= tuple(z)

#add two tuples
Laptops=("HP", "ASUS", "MAC")
Laptop=("DELL", )
Laptops+= Laptop
new_stock= Laptops + Laptop


print(Laptops)
print(Laptop)
#print(new_stock)