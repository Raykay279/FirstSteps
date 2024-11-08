bestellwert = float(input("Wie hoch ist der Bestellwert? "))

def endpreisberechnung(bestellwert, versandkosten):
    return bestellwert + versandkosten

try:
    if bestellwert <= 20:
        versandkosten = 5.00
        endpreis = endpreisberechnung(bestellwert, versandkosten)
        print(f"Dein Endpreis sind {endpreis:.2f}")
    elif bestellwert > 20 and bestellwert <= 100:
        versandkosten = bestellwert * 0.1
        endpreis = endpreisberechnung(bestellwert, versandkosten)
        print(f"Dein Endpreis sind {endpreis:.2f}")
    else:
        versandkosten = 0.00
        endpreis = endpreisberechnung(bestellwert, versandkosten)
        print(f"Dein Endpreis sind {endpreis:.2f}")
except ValueError:
    print("Bitte nur Zahlen eingeben!")

