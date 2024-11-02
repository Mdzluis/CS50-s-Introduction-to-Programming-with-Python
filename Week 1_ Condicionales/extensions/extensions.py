def main():
    name = input("File name: ").casefold().strip()

    extension(name)

def extension(n):
    if n.endswith(".gif") == True:
        print("image/gif")
    elif n.endswith(".jpeg") == True or n.endswith(".jpg") == True:
        print("image/jpeg")
    elif n.endswith(".png") == True:
        print("image/png")
    elif n.endswith(".pdf") == True:
        print("application/pdf")
    elif n.endswith(".txt") == True:
        print("text/plain")
    elif n.endswith(".zip") == True:
        print("application/zip")
    else:
        print("application/octet-stream")
main()
