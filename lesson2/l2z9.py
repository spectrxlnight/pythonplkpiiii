def x(y):
    if not y:
        return 0
    i = y.index(min(y))
    j = y.index(max(y))
    if i > j:
        i, j = j, i
    return sum(y[i+1:j])  
a = [3, 1, 4, 1, 5, 9, 2, 6]
print(x(a))  
