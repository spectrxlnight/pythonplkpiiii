lst = [3, 1, 4, 1, 5, 9, 1]
a = min(lst)
f = [i for i, x in enumerate(lst) if x == a]
print("індекси мінімальних елементів:", f)