def greet():
  print("Hello!!! Everyone")
greet()

def greet(name):
  print("Hello!!!", name)

greet("Sibangi")
greet("Seetal")
greet("Resma")

def user(name):
  print("Hello,", name, "Welcome to the world of Python")
  print("Enjoy learning Python")
user("Sibangi")
user("Seetal")
user("Resma")


def power(base, exponent):
  return base ** exponent
print("2 raised to the power of 3 is:", power(2, 3))

def add(a, b):
  return a + b
print("Sum of 5 and 3 is:", add(5, 3))

def multiply(a, b):
  return a * b
print("Product of 5 and 3 is:", multiply(5, 3))

def divide(a, b):
  if b == 0:
    return "Error: Division by zero is not allowed."
  return a / b
print("Division of 5 by 2 is:", divide(5, 2))

def subtract(a, b):
  return a - b
print("Subtraction of 5 and 3 is:", subtract(5, 3))

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)
print("Factorial of 5 is:", factorial(5))

def fibonacci(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    fib_sequence = [0, 1]
    for i in range(2, n):
      fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence
print("Fibonacci sequence of 10 numbers is:", fibonacci(10))

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True
print("Is 7 a prime number?", is_prime(7))