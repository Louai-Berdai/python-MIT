ecoles = ["École A", "École B", "École C", "École D", "École E"]
taux = [12.3, 8.7, 15.1, 6.2, 19.4]
moyenne = sum(taux) / len(taux)
print(f"La moyenne d'élèves qui décrochent dans les écoles est de {moyenne: .2f}%.")
print(f"L'école avec le taux de décrochage le plus élevé est {ecoles[taux.index(max(taux))]} avec {max(taux): .2f}%.")
print(f"L'école avec le taux de décrochage le plus bas est {ecoles[taux.index(min(taux))]} avec {min(taux): .2f}%.")