try:
  number = int(input("Enter a number:"))
  result = 100 / number
  print(result)
except ValueError:
  print("Thats not a valid number. Please enter a valid integer.")