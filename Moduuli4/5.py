i = 0
while i < 5:
    username = input("Käyttäjänimi: ")
    password = input("Salasana: ")
    if username == "python" and password == "rules":
        print("Tervetuloa")
        break
    else:
        i += 1
        if i == 5:
            print("Pääsy evätty")
            break
