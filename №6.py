import requests
from random import choice as random

response = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt")
data = response.text.split("\n")
while (True):
    s = input("Задайте вопрос. Если вопросов нет, напиште 'exit' ,чтобы закончить текущую ссесию \n")
    if (s == 'exit'):
        break
    else:
        print(random(data))
