lst = [3, 7, 2, 9, 5]
max = lst[0]
for x in lst[1:]:
    if x > max:
        max = x
print("Максимальний елемент:", max)