names = set()

while True:
    name = input("Nimi: ")
    if name == "":
        print(names)
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
