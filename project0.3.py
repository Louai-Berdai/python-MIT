import matplotlib.pyplot as plt

secteurs = {
    "Pierrefonds": [0.03, 0.06, 0.04, 0.07, 0.05],
    "DDO": [0.08, 0.09, 0.10, 0.11],
    "Pointe-Claire": [0.12, 0.08, 0.10],
    "Kirkland": [0.12, 0.02],
    "Beaconsfield": [0.07, 0.09]
}
noms = []
moyennes = []

for secteur, taux in secteurs.items():
    moyenne = sum(taux) / len(taux)
    noms.append(secteur)
    moyennes.append(moyenne * 100)
plt.bar(noms, moyennes)
plt.title("Taux de décrochage par secteur - West Island")
plt.xlabel("Secteur")
plt.ylabel("Taux de décrochage (%)")
plt.show()