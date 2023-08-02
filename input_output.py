# # input and out put in Python

# # Example 1
# name = input('Enter your name: ')
# print(name)

# # Example 2
# number = int(input('Enter a value : '))
# product = number * 10
# print(product)

# # Multiple inputs in Python
# s,r,w = map(int, input('Enter values: ').split())
# print('The values are :', end = "")
# print(s,r,w)

# W = (2,4,6,5,8)
# print("Current tuple")
# print(type(W))

# E = list(W)
# E.append(int(input("Enter a new value: ")))
# W = tuple(E)
# print("Updated tuple")
# print(W)

my_list = list(map(int, input("Enter list values: ").split()))
my_set = set(map(int, input("Enter set values: ").split()))

print(my_list)
print(my_set)
