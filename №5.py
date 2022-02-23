from random import choice as rand1
from random import randint as rand2
list = ['самовар', 'весна', 'лето']
r = rand1(list)
i = rand2(0, len(r) - 1)
ch = r[i]
print(r[0:i] + '?' + r[i + 1: len(r)])
s = input("Введите букву: ")
print('Победа!') if (s == ch) else print('Увы! Попробуйте в другой раз')
print(f'Слово: {r}')
