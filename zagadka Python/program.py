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
while userGuess != secret_number:

    if secret_number > userGuess:
        guess_amount -= 1
        print("Źle, ale mogę ci powiedzieć, że moja liczba jest większa.")


    else:
        guess_amount -= 1
        print("Źle, ale mogę ci powiedzieć, że moja liczba jest mniejsza.")

    userGuess = int(input("Zgaduj dalej: "))

    if userGuess == secret_number:
        print("Brawo mugolu! Jesteś teraz wolny.")
        print(guess_amount)

