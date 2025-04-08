#int, float and complex are number types
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

a = 35e3 #Float can also be scientific numbers with an "e" to indicate the power of 10.
b = 12E4
c = -87.7e100

print(type(a))
print(type(b))
print(type(c))

#Complex numbers are written with a "j" as the imaginary part
i = 3+5j
k = 5j
l = -5j

#Type Conversion - You can convert from one type to another with the int(), float(), and complex() methods:
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#Casting in python is therefore done using constructor functions
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'