calendario = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    fecha = input("introduce un mes: ").title()
    try:
        if fecha.find("/") != -1:
            mes, dia, año = fecha.split("/")
            if 1 <= int(mes) <= 12 and 1 <= int(dia) <= 31:
                print(f"{año}-{int(mes):02}-{int(dia):02}")
            else:
                continue

        elif fecha.find(",") != -1:
            mes, dia, año = fecha.split(" ")
            index = calendario.index(mes)+1
            dia = int(dia.replace(",",""))
            if 1 <= int(dia) <= 31:
                print(f"{año}-{index:02}-{dia:02}")
            else:
                continue
        else:
            continue
    except ValueError:
        pass
    else:
        break
