année_de_naissance = input("Entrez votre année de naissance:  ").strip()
nom = input("Entrez votre nom:  ").strip()
année_MIT = 2032
age = 2026 - int(année_de_naissance)
difference = année_MIT - int(année_de_naissance)
print(f"{nom}, votre age est de {age}ans. Il vous rest {difference} ans pour MIT.")