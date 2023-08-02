x="john"
y=2
z=1j

print(type(x))
print(type(y))
print(type(z))

## LISTS
#they are used to store many items in a single variable 
#ordered, changable, allows duplicates

Afternoon =[1,2,4,5,1]

print(Afternoon)
print(len(Afternoon))
print(type(Afternoon))
print(Afternoon[0])
print(Afternoon[-1])
print(Afternoon[2:4])
print(Afternoon[1:])
print(Afternoon[:4])
Afternoon.append(6)

Afternoon.insert(6,8)
#(index, value)

Afternoon.remove(2)
#(value you want to remove)

Afternoon.pop(2)
#(index)

print(Afternoon)
