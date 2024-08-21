nums = []

while True:
    num = input("Numero ")
    if num == "":
        break
    nums.append(int(num))

print(sorted(nums, reverse=True)[:5])
