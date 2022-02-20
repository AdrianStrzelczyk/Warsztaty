

def go():
    min = 0
    max = 1000
    for _ in range(10):
        guess = int((max - min) / 2) + min
        print(f"Zgaduję: {guess}")
        answer = input('Wpisz: "zgadłeś", "za dużo", "za mało": ')
        if answer == "zgadłeś":
            return "Wygrałem!"
        elif answer == "za dużo":
            max = guess
        elif answer == "za mało":
            min = guess
        else:
            print("nie oszukuj!")
    return "Przegrałem"


def guess():
    print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")
    while True:
        start = input("Gotowy? tak/nie: ")
        if start == "tak":
            return go()
        else:
            print("A teraz?")


print(guess())
