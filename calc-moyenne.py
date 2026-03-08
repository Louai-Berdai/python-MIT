maths = input("Entrez votre note en maths:  ").strip()
francais = input("Entrez votre note en francais:  ").strip()
histoire = input("Entrez votre note en histoire:  ").strip()
anglais = input("Entrez votre note en anglais:  ").strip()
sciences = input("Entrez votre note en sciences:  ").strip()
somme = int(maths) + int(francais) + int(histoire) + int(anglais) + int(sciences)
moyenne = somme / 5
if moyenne >= 90:
    print("Tu es sur la bonne trajectoire pour Dawson SIM")
elif moyenne >= 85:
    print("Tu es proche, mais tu dois améliorer")
else:
    print("Tu dois travailler plus fort")