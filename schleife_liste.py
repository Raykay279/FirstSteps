preise = [1.99, 2.99, 5.99, 11.99, 39.99]

gesamtpreis = 0

for i in preise:
    gesamtpreis += i

if gesamtpreis >= 50.00:
    rabatt = gesamtpreis * 0.1
else:
    rabatt = 0.00

endpreis = gesamtpreis - rabatt

print(f"Der Gesamtpreis liegt bei {endpreis:.2f} Euro. Der Rabatt dabei beträgt {rabatt:.2f} Euro")