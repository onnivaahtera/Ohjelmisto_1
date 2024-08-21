from random import randint


def throw_dice():
    return randint(1, 6)


while True:
    num = throw_dice()
    print(num)
    if num == 6:
        break
