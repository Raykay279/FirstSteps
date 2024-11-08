def gesamtkostenpreisbrechnung(menge, einzelpreis, versandkosten=5.0):
    gesamtkostenpreis = (menge * einzelpreis + versandkosten)
    return gesamtkostenpreis


menge = input("Bitte die Menge eingeben: ")
einzelpreis = input("Bitte den Einzelpreis eingeben: ")

gesamtpreis = gesamtkostenpreisbrechnung(int(menge), float(einzelpreis), versandkosten=50.00)
print("Der Gesamtpreis inkl. Versand beträgt: ", f"{gesamtpreis:.2f}", "Euro")

