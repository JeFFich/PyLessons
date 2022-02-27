from random import randint as random

def gen() -> str:
    leng = random(7, 10)
    a = []
    for i in range(leng):
        a.append(chr(random(33, 126)))
    return ''.join(a)

def check(s: str) -> bool:
    c1 = c2 = c3 = False
    if (len(s) > 7):
        for i in s:
            c1 = c1 or i.isupper()
            c2 = c2 or i.islower()
            c3 = c3 or i.isdigit()
    return (len(s) > 7 and c1 and c2 and c3)

c = 0
while True:
    c += 1
    s = gen()
    if (check(s)):
        print(s + "\n Номер попытки: " + str(c))
        break
