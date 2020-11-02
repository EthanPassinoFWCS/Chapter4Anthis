pizzas = ["cheesepizza", "pepperonipizza", "sasagepizza"]

for pizza in pizzas:
  print(f"I like {pizza}")

print("I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append("pizzapie")
friend_pizzas.append("Hawaiianpizza")

print("MY favorite pizzas are:")
for pizza in pizzas:
  print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
  print(pizza)

