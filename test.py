import random

secret = random.randint(1, 10)
guess = int(input("Devine un nombre entre 1 et 10 : "))

if guess == secret:
    print("Bravo, tu as trouvé !")
else:
    print("Raté, le nombre était", secret)