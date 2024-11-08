einkaufswagen = {
    "Apfel": {"menge": 5, "preis": 0.80},
    "Banane": {"menge": 2, "preis": 1.20 },
    "Pflaumen": {"menge": 1, "preis": 14.90},
    "Kaffe": {"menge": 1, "preis": 3.99},
    "Schokolade": {"menge": 4, "preis": 0.70}
}

einkaufswagen_nach_rabatt = {}

gesamter_warenkorb = 0

def berechnung_schlusspreis(gesamter_warenkorb,versandkosten):
    return gesamter_warenkorb + versandkosten

for produkt, details in einkaufswagen.items():
    menge = details["menge"]
    preis = details["preis"]

    if preis <= 2.0:
        endpreis = preis * 0.95
    elif preis  >= 10.00:
        endpreis = preis * 0.90
    else:
        endpreis = preis
    
    endpreis_gesamt = endpreis * menge

    einkaufswagen_nach_rabatt[produkt] = {"preis_nach_rabatt": endpreis, "menge": menge}

    gesamter_warenkorb += endpreis_gesamt

if gesamter_warenkorb <= 50.00:
    versandkosten = 5.00
else:
    versandkosten = 0.00

schlusspreis = berechnung_schlusspreis(gesamter_warenkorb,versandkosten)

print("Produkte vor dem Rabatt", einkaufswagen)
print("Produkte nach dem Rabatt", einkaufswagen_nach_rabatt)        

print("Der abschließende SChlusspreis beträgt: ", schlusspreis, "Euro")

