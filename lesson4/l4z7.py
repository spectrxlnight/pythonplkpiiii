c = int(input("Введіть ціле число: "))
if c % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")



a = int(input("Введіть свій вік: "))
if a >= 18:
    print("Ви повнолітні!")
else:
    print("Ви неповнолітній!")



import math

радіус = float(input("введіть радіус кола: "))

площа = math.pi * радіус ** 2
довжина = 2 * math.pi * радіус
print(f"площа кола: {площа:.2f}")
print(f"довжина кола: {довжина:.2f}")



a = float(input("введіть перше число: "))
b = float(input("введіть друге число: "))
if a > b:
    print(f"більше число: {a}")
elif b > a:
    print(f"більше число: {b}")
else:
    print("числа рівні")
