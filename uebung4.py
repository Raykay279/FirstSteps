with open("todos.txt", "r") as datei:
    for zeile in datei:
        print(zeile.strip())


new = input("Bitte ergänzen sie ein Todo: ")
new = new + "\n"


with open("todos.txt", "a") as datei:
    datei.write(new)


print("Hier die aktuelle Liste:")

with open("todos.txt", "r") as datei:
    for zeile in datei:
        print(zeile.strip())