# definim o metoda care poate primi nr variabil de argumente si ne returneaza suma acestora
def adunare(*args):
    suma = 0
    for arg in args:
        suma = suma + arg

    return suma


# apelam metoda 3 argumente
print(adunare(1, 2, 3))

tuplu = (1, 2, 3)

# incercam sa apelam metoda cu un tuplu care are 3 elemente - EROARE
# print(adunare(tuplu))

# Pentru a putea apela metoda cu toate elementele din tuplu, trebuie sa-l despachetam (in engleza: unboxing)
# Termenul "despachetare" se referă la procesul de separare a elementelor unui obiect iterabil
# (cum ar fi o listă sau un tuplu) și atribuirea lor individuală unor variabile separate.
# Despachetarea permite extragerea valorilor individuale din obiectul iterabil și utilizarea lor în mod independent.
print(adunare(*tuplu))


