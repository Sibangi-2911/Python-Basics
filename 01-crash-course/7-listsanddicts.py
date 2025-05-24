items = [1, 2, 3, "Sibangi", "Seetal", "Resma", True, False, 1.5, 2.5]
print(items)

numbers = [1, 2, 3, 4, 5]
print(numbers[0])
numbers[1]= 10
print(numbers)
numbers.append(6)
numbers.remove(3)
print(numbers)
numbers.insert(2, 20)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))
print(max(numbers))


#slicing lists
numbers= [1, 2, 3, 4, 5]
print(numbers[0:3])  # prints first three elements
print(numbers[2:])  # prints elements from index 2 to end
print(numbers[::2])  # prints every second element
print(numbers[::-1])  # prints the list in reverse order
print(numbers[-1])  # prints the last element
print(numbers+[6,7,8])  # concatenates two lists
print(numbers*2)  # repeats the list twice


#Dictionaries
student= {
"name": "Sibangi",
"age": 22,
"city": "Bangalore",
"subjects": ["Math", "Science", "English"],
"grades": {"Math": 90, "Science": 85, "English": 88}
}
print(student)
print(student["name"])
student["age"]= 23
student["city"]= "London"
student["subjects"].append("History")
student["grades"]["History"]= 95
print(student)
print(student.keys())
print(student.values())
print(student.items())