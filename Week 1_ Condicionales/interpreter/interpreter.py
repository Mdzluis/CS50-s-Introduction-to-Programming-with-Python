expresion = input("Expresion: ").strip()

x, y, z = expresion.split(" ")
x = float(x)
z = float(z)
match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)
