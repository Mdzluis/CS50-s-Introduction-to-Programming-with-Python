def main():
    prueba = input("Diga? ").casefold().strip()
    print(f"{value(prueba)}$")

def value(greeting):
    x = greeting.startswith("hello")
    y = greeting.startswith("h")
    if x == True:
        return 0
    elif x == False and y == True:
         return 20
    else:
        return 100

if __name__ == "__main__":
    main()
