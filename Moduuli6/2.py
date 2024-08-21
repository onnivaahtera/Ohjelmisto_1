from random import randint


def throw_dice(num):
    return randint(1, num)


num = int(input("Nopan tahkojen määrä: "))
while True:
    dice = throw_dice(num)
    print(dice)
    if num == dice:
        break
