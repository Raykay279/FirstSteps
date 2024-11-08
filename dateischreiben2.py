with open ("todos.txt", "w") as datei:
    datei.write("Hier sind die ToDos für heute\n")
    datei.write("1. Workshop vorbereiten\n")
    datei.write("2. Toilletengang\n")
    datei.write("3. Feierabend\n")

print("Datei mit der Bezeichnung todos.txt ist erstellt!")