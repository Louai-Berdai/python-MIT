Nombre1 = float(input("Entrez le premier nombre:  "))
Nombre2 = float(input("Entrez le deuxième nombre:  "))
operateur = input("Entrez l'opérateur (+, -, *, /):  ")
resultat = None
if operateur == '+':
    resultat = Nombre1 + Nombre2
elif operateur == '-':
    resultat = Nombre1 - Nombre2
elif operateur == '*':
    resultat = Nombre1 * Nombre2
elif operateur == '/':
    if Nombre2 != 0:
        resultat = Nombre1 / Nombre2
    else:
        print("Erreur: Division par zéro.")
else:
    print("Erreur: Opération non reconnue.")
if not resultat is None:
 print(f"Le résultat de {Nombre1} {operateur} {Nombre2} est: {resultat}")