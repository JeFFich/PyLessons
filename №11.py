import re

text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
lst = re.split('\n', text)
print(lst)
lst = list(map(lambda x: x.split(), text.split('\n'))) #разбиение на список слов
# 1 способ
print(list(map(lambda x: [i for i in x if len(i) > 3], lst)))
# 2 способ (без использования map и лямбда-выражений)
answ = []
for i in range(len(lst)):
    answ.append([x for x in lst[i] if len(x) > 3])
print(answ)
