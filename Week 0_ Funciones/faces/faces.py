def convert(dato):
    dato = dato.replace(":)","\N{slightly smiling face}").replace(":(","\N{slightly frowning face}")
    print(dato)
def main():
    entrada = input("")
    convert(entrada)
main()
