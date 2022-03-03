from statistics import mean
from statistics import median

lst = [1, -100, 10, 50, 56, 7, 0]
max_i = lst.index(max(lst))
min_i = lst.index(min(lst))
if (max_i > min_i):
    print(mean(lst[min_i + 1: max_i]))
else:
    print(lst[:max_i + 1] + [median(lst[max_i + 1: min_i]) for x in range(max_i + 1, min_i)] + lst[min_i:])

