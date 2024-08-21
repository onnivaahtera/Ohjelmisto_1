seasons = ("spring", "summer", "autumn", "winter")

month = int(input("Kuukausi: "))
if month >= 3 and month <= 5:
    print(seasons[0])
elif month >= 6 and month <= 8:
    print(seasons[1])
elif month >= 9 and month <= 11:
    print(seasons[2])
else:
    print(seasons[3])
