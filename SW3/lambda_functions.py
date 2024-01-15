"""
O functie lambda, este o functie anonima
care ia unul sau mai multe argumente si are
o singura expresie

- SYNTAX: lambda arguments: expression

- Expresia este executata si resultatul acesteia este returnat.

- Exemplul 1:
x = lambda a: a + 10
print(x(5))

- Exemplul 2:
result = lambda x, y: x + y
print(result(2, 3))

- Exemplul 3:
este_par = lambda x: x % 2 == 0
print(este_par(4))
print(este_par(5))

"""

# - Exemplul 1:
x = lambda a: a + 10
print(x(5)) # 15
print(x(10)) # 20

# - Exemplul 2:
result = lambda x, y: x + y
print(result(2, 3)) # 5
print(result(10, 60)) # 70

# - Exemplul 3:
este_par = lambda x: x % 2 == 0
print(este_par(4))
print(este_par(5))