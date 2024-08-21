airports = dict()

while True:
    user_input = int(input("1) Enter a new airport\n2) Fetch airport\n3) quit\n"))

    match user_input:
        case 1:
            airport_icao = input("airport ICAO code: ")
            airport_name = input("name of the airport: ")
            airports[airport_icao] = airport_name
        case 2:
            fetch_airport = input("airport ICAO code: ")
            for icao in airports:
                if icao == fetch_airport:
                    print(f"Airport name: {airports[icao]}\n")

        case 3:
            break
