import random
print("RECIPE GENERATOR")

proteins = ["chicken", "beef", "tofu", "fish", "pork", "lentils", "beans", "quinoa", "eggs"]
veggies = ["broccoli", "carrots", "spinach", "bell peppers", "zucchini", "cauliflower", "peas", "kale"]
carbs = ["rice", "pasta", "bread", "quinoa", "potatoes", "couscous", "polenta"]
methods = ["grilled", "baked", "stir-fried", "roasted", "steamed", "sautéed"]
flavours = ["spicy", "sweet", "savory", "herb-infused", "smoky", "citrusy"]
while True:
  protein = random.choice(proteins)
  veggie = random.choice(veggies)
  carb = random.choice(carbs)
  method = random.choice(methods)
  flavour = random.choice(flavours)
  print(f"Your random recipe is : {flavour} {method} {protein} with {veggie} and {carb}.")
  print("Generate another recipe? (y/n): ")
  answer = input().lower()
  if answer == 'n':
    print("👋 Goodbye!")
    break