import random

def main():
    # VARIABLE DECLARATION
    intents = 0
    point = 0
    level = get_level()
    while True:
        error = 0
        number1, number2 = generate_integer(level)
        while True:
            try:
                player = int(input(f"{number1} + {number2} ="))
            except ValueError:
                print("EEE")
                pass
            if player != (number1 + number2):
                error += 1
                print("EEE")
                if error == 3:
                    print(f"{number1} + {number2} = {number1 + number2}")
                    intents += 1
                    error = 0
                    break
            else:
                intents += 1
                point += 1
                break
        if intents == 10:
            print("Score:",point)
            break


# GET NIVEL OF GAME
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1,2,3]:
                return n
        except ValueError:
            print("EEE")


# GENERATION OF RANDOM NUMBERS
def generate_integer(level):
    try:
        if level == 1:
            number1 = random.randint(0, 9)
            number2 = random.randint(0, 9)
            return(number1, number2)
        elif level == 2:
            number1 = random.randint(10, 99)
            number2 = random.randint(10, 99)
            return(number1, number2)
        elif level == 3:
            number1 = random.randint(100, 999)
            number2 = random.randint(100, 999)
            return(number1, number2)
    except ValueError:
        print("EEE")

if __name__ == "__main__":
    main()
