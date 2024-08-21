from random import randint

number = randint(1, 10)

while True:
    guess = int(input("Numero: "))

    if guess < number:
        print("Liian pieni")
    elif guess > number:
        print("Liian suuri")
    else:
        print("Oikein!")
        break
