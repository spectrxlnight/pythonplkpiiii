w = 10
h = 5
c = '*'
z = '-'
for i in range(h):
    for s in range(w):
        if i == 0 or i == h-1 or s == 0 or s == w-1:
            print(c, end='')
        else:
            print(z, end='')
    print()  
