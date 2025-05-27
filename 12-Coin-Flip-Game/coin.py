import random
print("COIN FLIP GAME")
print("Guess heads or tails!!!")
while True:
  coin_choice = input("Enter your guess (heads/tails): ")
  if coin_choice.lower() not in ["heads","tails"]:
    print("Sorry!!! You have an invalid choice.")
  if coin_choice.lower() in ["heads", "tails"]:
    coin_flip = random.choice(["heads", "tails"])
    print(f"The coin shows: {coin_flip}")
    if coin_choice.lower() == coin_flip:
      print("You guessed correctly! 🎉 You win...")
    else:
      print("Sorry, you guessed wrong. 😢 You lose... Try again")
  play_again = input("Play again? (yes/no): ")
  if play_again.lower()!= "yes":
    print("Thanks for playing! 👋 Goodbye!")
    break