produkte_liste = {
    "Apfel": 2,
    "Banane": 1.5,
    "Pflaume": 12,
    "Kaffee": 8,
    "Schokolade": 15
}

def filter_produkte(x_dict, minpreis):
    return {produkte1 : preis1 for produkte1, preis1 in x_dict.items() if preis1 >= minpreis}


neues_dictionary = filter_produkte(produkte_liste, 10)
print(neues_dictionary)
