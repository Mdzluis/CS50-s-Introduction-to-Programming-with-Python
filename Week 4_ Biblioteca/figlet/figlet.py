import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()

# LISTA  DE FUENTES
list_fuentes = figlet.getFonts()

#   SELECCION DE FUENTE AL AZAR
if len(sys.argv) == 1:
    print("Condicion 1")
    fuente = Figlet(font = choice(list_fuentes))
    print(fuente.renderText(input("Input: ")))

#   SELECCION DE FUENTE DETERMINADA
elif 1 < len(sys.argv) < 4:
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in list_fuentes:
        sys.exit(1)
        print("Invalid usage")
    else:
        fuente = Figlet(font = sys.argv[2])
        print(fuente.renderText(input("Input: ")))





