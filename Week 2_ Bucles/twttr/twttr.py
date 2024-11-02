def main():
   palabra = input("Input: ")
   print("Output: ",end="")
   frase = shorten(palabra)
   print(frase)

def shorten(word):
    frase = ""
    for i in word:
        if not i.lower() in ["a", "e", "i", "o", "u"]:
            frase += i
    return frase



if __name__ == "__main__":
    main()
