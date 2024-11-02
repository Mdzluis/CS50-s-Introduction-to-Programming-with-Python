palabra = input("camelCase: ").strip()

print("snake_case: ", end="")
for i in palabra:
    if i.islower() == True:
        print(i, end="")
    else:
        print("_",i.lower(), end="",sep="")
print()
