import math
def area_circle(radius):
    return math.pi * radius ** 2
def area_rectangle(a, b):
    return a * b
def area_triangle(base, height):
    return 0.5 * base * height
print("оберіть фігуру для обчислення площі:")
print("1 - коло")
print("2 - прямокутник")
print("3 - трикутник")

choice = input("Ваш вибір (1/2/3): ")

if choice == "1":
    r = float(input("введіть радіус кола: "))
    print("площа кола =", area_circle(r))
elif choice == "2":
    a = float(input("введіть довжину: "))
    b = float(input("ведіть ширину: "))
    print("площа прямокутника =", area_rectangle(a, b))
elif choice == "3":
    base = float(input("введіть основу трикутника: "))
    height = float(input("введіть висоту трикутника: "))
    print("площа трикутника =", area_triangle(base, height))
else:
    print("помилка: невірний вибір!")
