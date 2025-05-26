import random
import math
import datetime
import os
import sys
import time

# Random number generation
random_number = random.randint(1,10)
print("Random number between 1 and 10:", random_number)

#choose a random element from a list
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print("Randomly selected fruit:", random_fruit)

# shuffle a list
random.shuffle(fruits)
print("Shuffled fruits:", fruits)

# generate a random float
random_float = random.uniform(1.0, 10.0)
print("Random float between 1.0 and 10.0:", random_float)
# generate a random sample from a list  
sample_fruits = random.sample(fruits, 2)
print("Random sample of 2 fruits:", sample_fruits)

print(math.pi)
print(math.sqrt(16))
print(math.factorial(5))
print(math.pow(2, 3))
print(math.floor(5.7))
print(math.ceil(5.7)) #6
print(math.sin(math.pi/2))
print(math.cos(math.pi))
print(math.tan(math.pi/4))
print(math.log(100, 10)) # log base 10
print(math.log(100)) # log base e

# datetime module
current_time = datetime.datetime.now()
print("CURRENT TIME:", current_time)
print("Current date:", current_time.date())
print("Current time:", current_time.time())
print("Current year:", current_time.year)
print("Current month:", current_time.month)

#os module
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")
print(f"List of files in current directory: {os.listdir('.')}")

#time module
print("Waiting for 2 deconds...")
time.sleep(2)
print("Waited for 2 seconds")

#sys module
print(f"Python Version: {sys.version}")
print(f"Platform: {sys.platform}")