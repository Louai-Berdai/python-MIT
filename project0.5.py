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
couleurs = []
for m in moyennes:
    if m < 6:
        couleurs.append('green')
    elif m < 9:
        couleurs.append('yellow')
    else:
        couleurs.append('red')

plt.bar(noms, moyennes, color=couleurs)
plt.title("Taux de décrochage par secteur - West Island")
plt.xlabel("Secteur")
plt.ylabel("Taux de décrochage (%)")
for i, v in enumerate(moyennes):
    plt.text(i, v + 0.1, f"{v:.2f}%", ha='center')
moyenne_globale = sum(moyennes) / len(moyennes)
plt.axhline(y=moyenne_globale, color='black', linestyle='--', label=f'Moyenne globale: {moyenne_globale:.2f}%')
plt.legend()
plt.show()