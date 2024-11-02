lista = []
while True:
    dic = {}
    try:
        ingrediente = input().upper()
        lista.append(ingrediente)
    except EOFError:
        print()
        for i in range(len(lista)):
            for j in range(len(lista)):
                j = lista.count(lista[i])
            dic.update({lista[i]:j})
        for x, y in sorted(dic.items()):
            print(y, x)
        break
