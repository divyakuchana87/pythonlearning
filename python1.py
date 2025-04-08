print("Hello World")
print(5+5)
print(5*2)

#Comments starts with a #, and Python will ignore them
#Python does not really have a syntax for multiline comments.
#To add a multiline comment you could insert a # for each line

#Python - Syntax 
#Python Indentation - Indentation refers to the spaces at the beginning of a code line.
if 5>2:
    print("five is greater than 2") #if no indentation, Syntax Error. 

#Variables
x = 5 #integer
y = "John" #string
print(x)
print(y)

#to fetch location/address where the data stored.
print(id(x))

x = 45
print(x)
print(id(x))

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = "Divya"
print(x)

#If you want to specify the data type of a variable, this can be done with casting.
x = str(3) # x will be '3' string
y = int(4) #y will be 4 integer
z = float(3.2466) #z will be 3.0
print(z)

#to find type of a variable - use type(variable name)
print(type(x)) #<class 'str'>
print(type(y)) #<class 'int'>
print(type(z)) #<class 'float'>

#String variables can be declared either by using single or double quotes:

a = "John"
# is the same as
a = 'John'

#Variable names are case-sensitive.
#This will create two variables:

b = 4
B = "Sally"
#B will not overwrite b
print(B)
print(b)

#Python allows you to assign values to multiple variables in one line
x, y, z = "orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange" #assign same value to multiple varaiables
#Unpack a Collection
fruits = ["orange", "Banana", "Cherry"] #list or tuple
x, y, z = fruits
print(x)
print(y)
print(z)
#Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
#when you try to combine a string and a number with the + operator, Python will give you an error
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types
x = 5
y = "Divya"
print(x, y)

#Global variables - Global variables can be used by everyone, both inside of functions and outside.
x = "awesome" #Create a variable outside of a function, and use it inside the function
def myfunc():
  print("Python is " + x)

myfunc() #Python is awesome

#Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
   x = "fantastic"
   print("Python is "+x)
myfunc()

print("Python is "+x)

def myfunc():
  global x #global keyword
  x = "super"
myfunc()
print("Python is " + x)

w = "awesome"
print(w)
def myfunc():
  global w
  w = "fantastic"
  print(w)
myfunc()
print("Python is " + w) #Python is fantastic
