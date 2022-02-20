import random


def check():
    comp_number = random.randint(1, 100)
    while True:
        try:
            user_number = int(input("Guess the number: "))
            if user_number == comp_number:
                return "You win!"
            elif user_number < comp_number:
                print("Too small!")
            elif user_number > comp_number:
                print("Too big!")
        except ValueError:
            print("It's not a number")


print(check())
