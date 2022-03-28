import requests

response = requests.get("http://dfedorov.spb.ru/python3/src/romeo.txt")
data = response.text.split()
count = dict.fromkeys(set(data), 0)
for i in data:
    count[i] += 1
print(count)
