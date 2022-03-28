import requests
import matplotlib.pyplot as plt
from statistics import mean

response = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat")
data = [float(i) for i in response.text.split("\n") if (i != "")]
m1 = max(data)
m2 = min(data)
m0 = round(mean(data), 1)
print(f'Максимальное значение -  {m1},  минимальное значение - {m2}, среднее значение - {m0}')
plt.plot(list(range(len(data))), data)
plt.show()
