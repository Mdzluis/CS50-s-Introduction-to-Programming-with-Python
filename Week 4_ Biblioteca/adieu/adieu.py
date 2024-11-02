import inflect
p = inflect.engine()

lista = []
while True:
    try:
        nombre = input("name: ").title()
        if nombre not in lista:
            lista.append(nombre)
            lista_nueva = p.join(lista)
    except EOFError:
        print()
        print("Adieu, adieu, to",lista_nueva,"\n")
        break
