lagerbestand = {
    "Teller": {"groesse": "a", "menge": 50.00, "preis": 12.00},
    "Löffel": {"groesse": "a", "menge": 230.00, "preis": 6.00},
    "Gabeln": {"groesse": "b", "menge": 523.00, "preis": 3.50},
}

gesamtwarenbestand  = 0

def gesamtwertberechnung(menge, preis):
    return  menge * preis

for produkt, details in lagerbestand.items():
    groesse = details["groesse"]
    menge = details["menge"]
    preis = details["preis"]

    print(f"{produkt}: Größe {groesse}, Menge {menge}, Preis {preis}")

    gesamtwert = gesamtwertberechnung(menge, preis)

    print(f"Der gesamtwert für das Produkt {produkt} ist {gesamtwert:.2f} Euro")
    gesamtwarenbestand += gesamtwert


print(f"Der Gesamtwartenbestand ist {gesamtwarenbestand:.2f}")
