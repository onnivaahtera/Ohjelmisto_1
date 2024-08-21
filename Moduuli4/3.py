numbers = []

while True:
  number = input("Numero: ")
  if number == "":
    break
  numbers.append(number)

print(numbers)
print(min(numbers), max(numbers, key=int))
  