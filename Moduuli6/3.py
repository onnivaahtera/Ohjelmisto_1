def gallons_to_liter(gallon):
    return gallon * 3.785


while True:
    gallons = int(input("Bensan määrä nestegallonoina: "))
    if gallons < 0:
        break
    print(gallons_to_liter(gallons))
