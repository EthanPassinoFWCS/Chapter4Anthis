numbers = [value for value in range(3, 30, 3)]

for num in numbers:
  print(num)

print("The first three items in the list are:")

for num in numbers[0:3]:
  print(num)
print("The three middle items of the list are:")

for num in numbers[int(len(numbers)/2) - 1:int(len(numbers)/2) + 2]:
  print(num)

print("The last three items are:")

for num in numbers[len(numbers)-3:]:
  print(num)
