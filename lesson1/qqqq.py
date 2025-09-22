import math
n = int(input("введіть ціле число n: "))
if n < 0:
    print("ні — від'ємне число не може бути досконалим квадратом.")
else:
    k = int(math.sqrt(n))
    if k * k == n or (k+1)*(k+1) == n:
        print(f"{n} є досконалим квадратом (={ (k if k*k==n else k+1) }^2).")
    else:
        print(f"{n} не є досконалим квадратом.")
