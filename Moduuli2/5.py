leiviska = float(input("Leiviska: "))
naula = float(input("Naula: "))
luoti = float(input("Luoti: "))

gramma = 13.3
naula_gramma = gramma * 32
leiviska_gramma = naula_gramma * 20

sum = (luoti * gramma) + (leiviska * leiviska_gramma) + (naula * naula_gramma)


print("Massa nykymittojen mukaan:")
print(f"{int(sum / 1000)} Kilogrammaa ja {round(float(sum % 1000), 2)} Grammaa")


