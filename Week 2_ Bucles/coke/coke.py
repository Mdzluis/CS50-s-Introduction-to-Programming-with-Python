def main():
    cock = 50
    while cock > 0:
        print("Amount Due:",cock)
        monto = pago(cock)
        cock = cock - monto
        if cock < 0:
            print("Change Owed:",cock*(-1))
        elif cock == 0:
            print("Change Owed:",cock)

def pago(cock):
    while True:
        n = int(input("Insert Coin: "))
        if n == 5 or n == 10 or n == 25:
            break
        else:
            print("Amount Due:",cock)
            continue
    return n
main()
