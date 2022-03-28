file = open('moby_clean.txt', 'r')
text = file.read().split("\n")
data = {}
for line in text:
    if line in data.keys():
        data[line] += 1
    else:
        data[line] = 1
data = sorted(data, key = lambda x: data.get(x))
print(f'5 самых редких - {data[:5]}, 5 самых частых - {data[:len(data) - 6:-1]}')
