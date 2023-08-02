# -------------------CONTROL FLOW----------------------

# conditional statements

# if-else statement

x = 1
if x == 1:
    print("Hello world")
else:
    print("Goodbye world")


x = 2
if x == 1:
    print("Hello world")
elif x == 2:
    print("Goodbye world")
else:
    print("See you later")


# Example 1

age = 12
if (age < 18):
    print("You are underage")
elif (age >= 18 and age <= 65):
    print("You are adult")
else:
    print("You are senior citizen")

# OR

'''
age = int(input())
if (age < 18):
    print("You are underage")
elif (age >= 18 and age <= 65):
    print("You are adult")
else:
    print("You are senior citizen")

'''

# -----------------------LOOPS-----------------------

# for loop

for x in range(5, 10):
    print(x)

cars = ["tesla", "jeep", "ford", "toyota", "BMW"]
for car in cars:
    print(car)

fruits = ("banana", "jackfruit", "kiwi", "lemon")
for fruit in fruits:
    print(fruit)

# while loop

x = 1
while x <= 10:
    print(x)
    x += 1


fruits = ["banana", "jackfruit", "kiwi", "lemon"]
while fruits:
    print(fruits)
    fruits = fruits[1:]


fruits = ["banana", "jackfruit", "kiwi", "lemon"]
counter = 0
while counter < len(fruits):
    print(fruits[counter])
    counter += 1

# ----------BREAK AND CONTINUE STATEMENTS-------------
# break statement

for x in range(10):
    if x == 5:
     break
    print(x)

# continue statement

numbers=[1,2,4,5,6]
for x in numbers:
    if x % 2 == 0:
        continue
    print(x)


# -------EXCEPTION HANDLING (try, except, finally)--------

    try:
        print(1/0)
    except ZeroDivisionError:
        print("Error: division by zero")
    finally:
        print("thank you")


    numbers=[1,2,3,4,5]
    try:
        print(numbers[9])
    except IndexError:
        print("WRONG INDEX PLEASE")
    finally:
        print("Final")

#---------------------DICTIONARY-------------------- 
# dict is a dictionary (stores information in key value pairs)

# Example 5
emotions = { "happy" : "I'm glad to hear you're happy",
                 "sad":  "I'm sorry to hear that youre feeling sad",
                 "angry": "take a deep breath and try to stay alive",
                 "fearful": "I understand that fear can be challenging",
                 "disgusted": "That's unfortunate to feel disgusted",
                 }
# prompt user to enter their emotions
user_emotion = input("How are you feeling today? ")

# convert the user input to lowwer case
user_emotion = user_emotion.lower()


if user_emotion in emotions:
    print(emotions[user_emotion])
else:
    print("I don't understand the emotion")


#---------------------Exercise---------------------
scale = { 1 : "That is extremely bad",
                 2:  "That is very bad",
                 3: "That is bad",
                 4: "That is not good",
                 5: "That is fair",
                 6 : "That is not bad ",
                 7: "That is fairly good ",
                 8: "That is good ",
                 9: "That is Excellent ",
                 10: "That is Brilliant",
                 }
# prompt user to enter their emotions
user_emotion = int(input("On a scale of 1 to 10, Rate your mental health!"))


if user_emotion in scale:
    print(scale[user_emotion])
else:
    print("Enter a valid number")




