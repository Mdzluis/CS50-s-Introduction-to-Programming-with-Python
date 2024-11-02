signos = ["."," ",",",";",":","...","¡","!","¿","?","'","[","]","(",")"]
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if inicio_letra(s) == True:
        if longitud(s) == True:
            if buscar_numeros(s) == True:
                    return True
    else:
        return False

def inicio_letra(u):
    if u[0:2].isalpha() == True:
        return True
    else:
        return False

def longitud(x):
    ancho = len(x)
    if ancho < 2 or ancho > 6:
        return False
    else:
        return True

def buscar_numeros(z):
    if z.isalpha() == True:
        return True
    else:
        ancho = len(z)
        for i in range(ancho):
            if z[i].isnumeric() == True:
                if z[i] != "0":
                    if not z[i] in signos:
                        x = z[i]
                        index = z.index(x)
                        if z[index:ancho].isnumeric() == True:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
main()
