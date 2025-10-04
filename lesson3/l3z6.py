lst = [2, 6, 8, 3, 7, 5]
c = sum(1 for x in lst if x > 5)
print("Кількість > 5:", c)