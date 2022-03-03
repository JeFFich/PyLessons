from math import log as log

def my_log(lst: list) -> list:
    return list(map(lambda x: log(x) if (x > 0) else None, lst))

print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))
