import requests
import numpy

def coun(line):
    curr = numpy.array([0, 0, 0])
    for i in line:
        if (i.isupper()):
            curr += [1, 0, 0]
        elif (i.islower()):
            curr += [0, 1, 0]
        elif (i.isdigit()):
            curr += [0, 0, 1]
    return curr

response = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt")
data = response.text.split("\r\n")
answ = numpy.array([0, 0, 0])
for line in data:
    answ += coun(line)
print({"Кол-во символов в верхнем регистре": answ[0], "Кол-во символов в нижнем регистре": answ[1], "Кол-во цифр": answ[2]})
