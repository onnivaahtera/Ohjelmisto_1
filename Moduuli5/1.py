from random import randint

nums = []

dice = int(input("Arpakuutioiden lukumäärä "))

for i in range(dice):
    nums.append(randint(1, 6))
print(sum(nums))
