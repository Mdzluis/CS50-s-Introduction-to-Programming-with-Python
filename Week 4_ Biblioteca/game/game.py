# RANDOM AND SYS LIBRARY IMPORT
import random
import sys

# CONDITION OF NET POSITIVE NUMBER
def get_positive_number(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass

def main():
    level = get_positive_number("Level: ")

# NUMERICAL RIDDLE GENERATION
    number_win = random.randint(1, level)
    while True:

# WINNING NUMBER VERIFICATION
        number = get_positive_number("Guess: ")
        if number < number_win:
            print("Too small!")
        elif number > number_win:
            print("Too large!")
        else:
            print("Just right!")
            exit()

if __name__ == "__main__":
    main()




