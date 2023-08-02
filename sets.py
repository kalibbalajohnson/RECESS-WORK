#store multiple items in a single variable 
#unchangable but one can add and remove and add new items

setone = {"rice","matooke", "irish"}
print(setone)

#no duplicate values allowed
settwo = {"rice","matooke", "irish", "irish", "irish"}
print(settwo)


#Exercise legth of set,data type, accessing items in a set, add items, add 2 sets

#---------------------Exercise---------------------------
my_set = {"goat", "cow", "fish"}

#legth of set
print(len(my_set))
print("The length is " + str(len(my_set)))

#data type
print(type(my_set))

#  accessing items in a set
for item in my_set:
    print(item)


# Accessing a the first item by iterating over the set
for item in my_set:
    print(item)
    break

# checking if a value exists in a set
print("hen" in my_set)

#add items to set
my_set.add("rabbit")
print(my_set)


#adding two sets together
first_set = {7, 8, 9}
second_set = {10, 12, 13}
final_set = first_set.union(second_set)
print(final_set)

#OR

final_set = final_set | second_set
print(final_set)


#------------------------------------------------------------