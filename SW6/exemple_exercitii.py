lista_elemente = [
    [1, "test"],
    [2, "test1"],
    [3, "test2"]
]

for i in range(len(lista_elemente)):
    for j in range(len(lista_elemente[i])):
        print(f"Valoarea curenta a elementului din lista este: {lista_elemente[i][j]}")

lista_culori_disponibile = ["rosu", "galben", "albastru", "fuchsia", "magenta", "roz", "violet", "maro", "negru",
                            "orange", "verde", "indigo"]

liste_culori_de_exclus = ["rosu", "galben", "roz"]

for i in range(len(lista_culori_disponibile)):
    if lista_culori_disponibile[i] not in liste_culori_de_exclus:
        print(f"Va recomandam haina de culoare {lista_culori_disponibile[i]}")

# SAU

for i in range(len(lista_culori_disponibile)):
    if lista_culori_disponibile[i] in liste_culori_de_exclus:
        continue  # dam skip la restul instructiunilor din for
    print(f"Va recomandam haine in culoarea: {lista_culori_disponibile[i]}")

# continue este o modalitate prin care putem sa sarim peste iteratia curenta
# fara sa iesim din structura repetitiva

