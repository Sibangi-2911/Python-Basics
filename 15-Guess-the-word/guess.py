import random
print("WORD SCRAMBLE GAME")
print("Unscramble the letters to find the word!!!")
words = ["python","learn","scramble","meaning","feature","ridiculous","appetizer","standard","maintainence"]
while True:
  original_word = random.choice(words)
  letters = list(original_word)
  random.shuffle(letters)
  print(f"Scrambled word: {"".join(letters)}")
  input_word = input("What's the word? ")
  if input_word == original_word:
    print("Correct!!You win")
  else:
    print("Sorry the word was : "+ original_word)
  
  print("\n Play again (y/n)???")
  yes_no = input().lower()
  if yes_no != "y":
    print("Goodbyeeeeee")
    break

