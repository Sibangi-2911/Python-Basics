import math
try:
  while True:
    print("SIMPLE CALCULATOR")
    print("Select operation: \n 1. + Addition \n 2. - Substraction \n 3. x Multiplication \n 4. / Division")
    choice = int(input("Enter choice (1-4): "))
    if choice not in [1,2,3,4]:
      print("Invalid input. Please enter a valid number between 1 to 4")
    else:
      break
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    if choice == 1:
      result = first_num+second_num
      print(f"{first_num}+{second_num}={result}")
    elif choice == 2:
      result = first_num-second_num
      print(f"{first_num}-{second_num}={result}")
    elif choice == 3:
      result = first_num*second_num
      print(f"{first_num}*{second_num}={result}")
    elif choice == 4:
      if second_num==0:
        print("Denominator can't be zero")
      else:
        result = first_num/second_num
        print(f"{first_num}/{second_num}={result}")
    another_time = input("Do you want to perform another calculation? (yes/no) ")
    if another_time.lower() != 'yes':
      print("GoodByeeeeee")
      break

except ValueError:
  print("Please enter positive value")
except ZeroDivisionError:
  print("Division by zero is not allowed. Please enter a non-zero number.")