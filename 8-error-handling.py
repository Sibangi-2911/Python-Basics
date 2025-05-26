try:
  number = int(input("Enter a number:"))
  result = 100 / number
  print(result)
except ValueError:
  print("Thats not a valid number. Please enter a valid integer.")
except ZeroDivisionError:
  print("Division by zero is not allowed. Please enter a non-zero number.")
finally:
  print("This piece of code will always run.")