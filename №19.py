from statistics import mean

lst = [1, 5, 6.3, 6, None, 2.0, -4, None]
m = mean([x for x in lst if (x != None)])
print(list(map(lambda x: x if (x != None) else m, lst)))
