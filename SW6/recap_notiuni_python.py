"""
1. Ce este o variabila in Python?
"""
# O variabila in Python este o zona din memoria unui calculator in care putem
# stoca date.

# definirea unei variabile in Python
x = 10
nume_complet = "Pop Alina"

"""
2. Cum afisam un mesaj in consola?
"""
print("Ana a plecat.")
print(nume_complet)

"""
3. Ce tipuri de date cunosti?
"""

# int -> numar intreg
nr = 9

# string -> sir de caractere delimitat de ghilimele
x = "Ana a plecat"
nume = 'Ana Popa'
'Ana a spus "Vin repede."'

# bool -> True sau False (valoare de adevar)
inmatriculat = True
# inmatriculat = False

# float -> numar zecimal
pi = 3.14

"""
4. Cum putem extrage un subsir de caractere dintr-un string?
"""
nume = "Ana Popa"
print(nume[:3]) # Ana

# ultimul caracter din string
print(nume[-1])

"""
5. Caracterieaza urmatoarele structuri de date din punct de vedere
al mutabilitatii (mutabil/imutabil) si al ordonarii (ordonat/neordonat):
- liste
- dictionare
- tupluri
- seturi
"""

# liste
my_list = [True, "Ana", 2, 2.5]

# mutabila/imutabila => MUTABILA
# Putem modifica, adauga sau sterge elemente
my_list = my_list + ["Capsuni"]
print(my_list)

my_list.append("Kiwi")
print(my_list)

# ordonata/neordonata => ORDONATA
# Se pot accesa elementele dupa INDEX
# Elementele se salveaza in memorie in ordinea in care au fost adaugate
# Un element nou va fi mereu adaugat la finalul listei
print(my_list[2])

# dictionare
dictionar = {
    "Ana": 16,
    "Ioan": 30
}

# Este dictionarul mutabil/imutabil? => MUTABIL
dictionar.update({"Alina": 35})
print(dictionar)

dictionar["Alex"] = 17
print(dictionar)

# Este dictionarul ordonat/neordonat? => NEORDONAT

# tupluri
coordonate = (12.34, 25.67)
my_tuple = (12.34,)
print(type(my_tuple))

# Sunt tuplurile MUTABILE/IMUTABILE? => IMUTABILE


# Sunt tuplurile ORDONATE/NEORDONATE? => ORDONATE
print(coordonate[1])

# seturi

# Sunt seturile MUTABILE/IMUTABILE?  => MUTABILE, dar elementele din set sunt IMUTABILE
my_set = {"capsuni", 1, "ceva"}
print(my_set)

# adaugarea unei valori noi intr-un set
my_set.add("kiwi")
print(my_set)

# Sunt seturile ORDONATE/NEORDONATE? => NEORDONATE

"""
6. Ce este o exceptie in Python si cum o putem trata?
"""

# Exceptie = eroare/situatie in care nu poate fi executat codul
# my_set.add([1, 2])
print("hello")

# Cum ridicam o exceptie? => raise
# a = int(input("Numarul a: "))
# b = int(input("Numarul b: "))
#
# if b != 0:
#     print(a / b)
# else:
#     raise ZeroDivisionError

# Cum tratam o exceptie? => try/except


def add_element(set, element):
    try:
        set.add(element)
    except TypeError:
        print("Nu putem adauga elemente mutabile intr-un set")


add_element(my_set, [1, 2])


# my_set.add([1, 2])

"""
7. Ce sunt functiile in Python?
"""

# secvente de cod definite o singura data, si care
# pot fi refolosite de oricate ori dorim

"""
8. Ce sunt clasele in Python?
"""

# Clase in Python = un sablon dupa care se creeaza un obiect


# class ComandaVanzare
class Caine:

    rasa = "Golden Retriever"

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def say_hello(self):
        print("Ham ham")


caine1 = Caine(2, "Bob")
print(caine1.age)
print(caine1.name)
caine1.say_hello()


"""
9. Care sunt principiile OOP?
"""

# Principii OOP
# MOSTENIRE
# INCAPSULARE
# ABSTRACTIZARE
# POLIMORFISM

"""
10. Ce face blocul else atasat unui ciclu repetitiv?
"""

# for
my_list = [1, 2, 3, 4, 5]

for element in my_list:
    if element == 3:
        break
    print(element)
else:
    # codul care se executa la finalul unei iteratii
    # atata timp cat iteratia a ajuns la final/ NU a fost intrerupt
    print("bloc else for 1")

for i in range(1, 3):
    # print(f"Suntem la iteratia {i}")
    print("*" * i)

# while
nr = 0

while nr < 5:
    print("Numarul este mai mic decat 5")
    nr += 1

"""
11. Cum putem accesa o valoare dintr-un dictionar?
"""

# dupa cheie

# my_dict = {
#     "pret": 25,
#     "nume": "birou",
#     "culoare": "maro"
# }
#
#
# print(my_dict["nume"])

# print(my_dict["cantitate"])
# print(my_dict.get("cantitate", 0))
"""
12. Cum putem inversa un string?
"""
# my_str = "abcde"
# print(my_str[::-1])
# print(reversed(my_str))
# print(my_str)

"""
13. Care este diferenta dintre o interfata si o clasa abstracta?
"""

# interfata -> contine doar metode abstracte (metode fara implementare concreta)
# clasa abstracta -> contine atat metode abstracte cat si metode cu implementare concreta

"""
14. Ce reprezinta parametru self folosit in clase?
"""
x = int(2)
print(x)

for i in range(4,0,-2):
    print(i)