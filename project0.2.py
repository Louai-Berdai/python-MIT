secteurs = {
    "Pierrefonds" : [0.03, 0.06, 0.04, 0.07, 0.05],  # 5 écoles
    "DDO" : [0.08, 0.09, 0.10, 0.11],                 # 4 écoles
    "Pointe-Claire" : [0.12, 0.08, 0.10],             # 3 écoles
    "Kirkland" : [0.12, 0.02],                        # 2 écoles
    "Beaconsfield" : [0.07, 0.09],                    # 2 écoles
}
for secteurs, taux in secteurs.items():
    moyenne = sum(taux) / len(taux)
    print(f"Le taux de décrochage de {secteurs} est de {moyenne * 100: .2f}%.")
    print(f"Le secteur avec le taux de décrochage le plus bas est {secteurs} avec {min(taux) * 100: .2f}%.")
    print(f"Le secteur avec le taux de décrochage le plus élevé est {secteurs} avec {max(taux) * 100: .2f}%.")