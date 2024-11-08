preise = [2, 14, 16, 40, 516]

preisupdates = []


for i in preise:
    if i <= 10:
        preis_neu = i * 1.0
    elif i > 10 and i <30:
        preis_neu = i * 0.9
    else:
        preis_neu = i * 0.8
    preisupdates.append(preis_neu)

print(preise)
print(preisupdates)
