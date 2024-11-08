preisliste = [2, 13, 24, 35, 46]
angepasste_preisliste = []

for i in preisliste:
    if i < 20:
        angepasster_preis = i * 1.1
    else:
        angepasster_preis = i * 1.0

    angepasste_preisliste.append(angepasster_preis)

print("Originalpreis: ", preisliste)
print("Angepasste Preise: ", angepasste_preisliste)