import random


def lotto():
    while True:
        try:
            users_numbers = []
            comp_numbers = random.sample(range(1, 49), 6)
            comp_numbers.sort()
            while len(users_numbers) < 6:
                user_number = int(input("Podaj liczbę: "))
                if user_number in range(1, 49):
                    if user_number not in users_numbers:
                        users_numbers.append(user_number)
                    else:
                        print("Podałeś już taką liczbę")
                if user_number not in range(1, 49):
                    print("Liczba ma mieścić sie w przedziale 1-49")
            users_numbers.sort()
            print(f"Wybrałeś: {users_numbers}")
            check = []
            for number in users_numbers:
                if number in comp_numbers:
                    check.append(number)
            if len(check) in range(3, 6):
                return f"Wynik losowania to: {comp_numbers} \n Gratulacje! Trafiłeś {len(check)}!"
            else:
                return f"Wynik losowania to: {comp_numbers} \nNiestety, trafiłeś tylko {len(check)} :("
        except ValueError:
            print("To nie jest liczba!")


print(lotto())
