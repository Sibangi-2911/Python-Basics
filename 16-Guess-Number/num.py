import random
print("Welcome to the number guessing game!!!")
print("I am thinking of  number between 1 and 100. You have 10 attempts.")
while True:
  secret_number = random.randint(1,100)
  total_attempt = 10
  current_attempt=0
  while current_attempt<total_attempt and not False:
    current_attempt+=1
    try:
      guess = int(input(f"Attempt {current_attempt}/{total_attempt}.Enter your guess: "))
    except ValueError:
      print("PLease enter a valid number")
      continue
    if secret_number==guess:
      print(f"Congratulations!! You have the number {secret_number} in {current_attempt} attempts.")
      break
    if secret_number>guess:
      print("Too low!!! Try a higher number")
    if secret_number<guess:
      print("Too high!! guess a lower number")
  play_again = input("Play again? (yes/no): ")
  if play_again.lower()!= "yes":
    print("Thanks for playing! 👋 Goodbye!")
    break