import random

secret_number = random.randint(0, 100)
guess_amount = random.randint(5, 10)

print(
"""
+================================+
| Welcome to my game, muggle!    |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

userGuess = int(input("Podaj swój wybór: "))

while guess_amount > 0:

    if userGuess == secret_number:
        print("Brawo mugolu! Jesteś teraz wolny.")
        print("Pozostało ci jeszcze:", guess_amount, "prób.")
        break

    elif secret_number > userGuess:
        print("Źle, ale mogę ci powiedzieć, że moja liczba jest większa.")

    else:
        print("Źle, ale mogę ci powiedzieć, że moja liczba jest mniejsza.")

    guess_amount -= 1
    print("Pozostało ci:", guess_amount, "prób.")

    if guess_amount > 0:
        userGuess = int(input("Zgaduj dalej: "))

if guess_amount == 0 and userGuess != secret_number:
    print("Przegrałeś! Nie udało ci się zgadnąć liczby.")
    print("Sekretna liczba to:", secret_number)
