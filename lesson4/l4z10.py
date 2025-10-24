def x(a1, a2):
    count = 0
    for n in range(a1, a2 + 1):
        s = f"{n:06d}"
        if sum(int(c) for c in s[:3]) == sum(int(c) for c in s[3:]):
            count += 1
    return count
a1 = int(input("введіть число a1: "))
a2 = int(input("введіть число a2: "))
res = x(a1, a2)
print(f"кількість щасливих квитків: {res}")
