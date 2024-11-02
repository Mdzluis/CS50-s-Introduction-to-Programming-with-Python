def main():
    gasolina = input("Fraction: ")
    fuel = convert(gasolina)
    print(gauge(fuel))

def convert(fraction):
    x, y = fraction.split("/")
    fraction = round((int(x) / int(y))*100)
    # CONDITION 1
    if fraction > 100 or fraction == ValueError:
        raise ValueError
    # CONDITION 2
    elif int(y) == 0:
        raise ZeroDivisionError
    else:
        return fraction


def gauge(percentage):
    try:
        if 99 <= percentage <= 100:
            return "F"
        elif 0 <= percentage <= 1:
            return "E"
        else:
            return f"{percentage}%"
    except TypeError:
        return TypeError

if __name__ == "__main__":
    main()
