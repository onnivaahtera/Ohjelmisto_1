num = int(input("Numero: "))

if num <= 1:
    print("Luku ei ole alkuluku")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Luku ei ole alkuluku")
            break
    else:
        print("Luku on alkuluku")
