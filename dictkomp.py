lagerbestand = {
    "Teller": 120,
    "Tassen": 45,
    "Löffel": 200,
    "Gabeln": 15,
    "Gläser": 75 
}

verfuegbare_produkte = {produkt: bestand for produkt, bestand in lagerbestand.items() if bestand > 50}

print(verfuegbare_produkte)