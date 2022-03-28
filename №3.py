import requests

file = open('moby_clean.txt', 'w')
response = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt")
trantab = str.maketrans({".": None, "-": " ", ",": None, ";": None})
data = [s.upper() for s in response.text.translate(trantab).split()]
for s in data:
    file.write(s + "\n")
file.close()