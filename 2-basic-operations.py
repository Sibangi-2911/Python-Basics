import math
x = 5
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

first_name = "Sibangi"
last_name = "Boxipatro"
full_name = first_name + " " + last_name
print(full_name)
print(f"Hey!! My first name is {first_name} and my last name is {last_name}")


i = 5
j = 6
k = 7
print(i, j, k)

# Values are swapped
s = 5
t = 6
print("Values before swapping : ", s, t)
s, t = t, s
print("Values after swapping : ", s, t)

# Comparison Operators
c = 5
d = 10
print(c == d)
print(c != d)
print(c<d)
print(c>d)
print(c<=d)
print(c>=d)

#Logical Operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)

# string slicing [start index: stop index+1: step]
text = "Python Programming"
print(text[0:6]) #Python
print(text[7:]) #Programming
print(text[::-1]) #gnimmargorP nohtyP
print(text[0:6:2]) #Pton
print(text[::2]) #Pto rgamn

#string formatting with .format()
name = "Sibangi"
age = "20"
msg = "Hello my name is {} and my age is {} years.".format(name, age)
print(msg)

#using placeholders
msg2 = "Hello my name is {0} and my age is {1} years. {0} is a nice name.".format(name, age)
print(msg2)

# math module operations
print(math.pi)
print(math.sqrt(16))
print(math.factorial(5))
print(math.pow(2, 3))
print(math.floor(5.7))
print(math.ceil(5.7)) #6
print(math.sin(math.pi/2))
print(math.cos(math.pi))
print(math.tan(math.pi/4))

pi = 3.141592653589793238
print(round(pi , 2))
