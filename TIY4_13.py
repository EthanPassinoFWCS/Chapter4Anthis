foods = ("pizza", "macaroni", "steak", "hamburger", "spaghetti")

for food in foods:
  print(food)

  # foods[0] = "salad" this is the line that is meant to error
foods = ("pizza", "salad", "steak", "hamburger", "crab")

for food in foods:
  print(food)