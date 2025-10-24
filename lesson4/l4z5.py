def x(n):
    for digit in str(n):
        d = int(digit)
        if d == 0 or n % d != 0:  
            return False
    return True
N = int(input("Введіть N (10 < N < 9999): "))
print("числа які не перевищують", N, "та діляться на всі свої цифри:")
for i in range(10, N + 1):
    if x(i):
        print(i)