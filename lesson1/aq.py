import math
def y(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    r = int(math.sqrt(x))
    for d in range(3, r + 1, 2):
        if x % d == 0:
            return False
    return True

n = int(input("Введіть n: "))
primes = []
for i in range(2, n + 1):
    if y(i):
        primes.append(i)

print("Прості числа від 1 до", n, ":")
print(primes)
