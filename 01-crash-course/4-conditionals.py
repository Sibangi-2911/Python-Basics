temp = 40
if temp > 40:
  print("Extreme hot")
else:
  print("Not so extreme hot")

marks = 95
if marks>=60:
  print("You have passed")
  if marks>=90:
    print("Grade A")
  elif marks>=80:
    print("Grade B")
  elif marks>=70:
    print("Grade C")
  elif marks>=60:
    print("Grade D")
  else:
    print("Grade F")
else:
  print("You have failed")

# in operator
fruit = "apple"
if fruit in {"apple", "banana", "orange"}:
  print(f"{fruit} is in the list")

#Ternary operator
age = 19
status = "Adult" if age>=18 else "Minor"
print(f"Status:{status} ")