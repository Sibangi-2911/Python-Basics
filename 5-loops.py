# for loop
for i in range(1,6):
  print(i)

for i in range(5, 0, -1):
  print(i) 

# while loop
count= 1
while count<=5:
  print(count)
  count+=1

count = 5
while count>=1:
  print(count)
  count-=1

# loops in list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

for fruit in reversed(fruits):
  print(fruit)

#loop with enumerate
print("Fruit with indices: ")
for index, fruit in enumerate(fruits):
  print(f"{index}: {fruit}")

#loop with dictionaries
person = {"name":"Sibangi", "age":22, "city":"Bangalore"}
print("\n Person dict")
for key,value in person.items():
  print(f"{key}: {value}")

#list comprehensions: compact loop for creating lists
squares = [x==2 for x in range(1,6)]
print("printed squares from 1 to 5", squares)

#for loop with zip()
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "pink"]
for fruit,color in zip(fruits,colors):
  print(f"{fruit} is {color}")

for i in range(1,10):
  if i%2==0:
    continue
  print(i)  # prints only odd numbers

# break statement
for i in range(1,10):
  if i==5:
    break
  print(i)  # prints numbers until it reaches 5