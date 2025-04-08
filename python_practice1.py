#Write a Program to input 2 numbers & print their sum.
x = input("enter first number: ") #input function takes values from user
y = input("enter second number: ")
print("sum=", int(x)+int(y))

#WAP to input side of a square & print its area.
squaresides = float(input("enter sides: "))
print("area = ", squaresides * squaresides) 
print("area = ", squaresides **2) 

#WAP to input 2 floating point numbers & print their average.

first = float(input("enter first number: "))
second = float(input("enter second number: "))
print("average =", (first + second)/2)

#WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False.

a = int(input("enter a: "))
b = int(input("enter b: "))
print(a >= b)