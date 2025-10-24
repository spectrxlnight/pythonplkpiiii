a = int(input("введіть ваш вік: "))
if 1 <= a <= 120:
    last= a % 10
    p = (a // 10) % 10
    if p == 1:
        w = "років"
    elif last == 1:
        w = "рік"
    elif 2 <= last <= 4:
        w = "роки"
    else:
        w = "років"
    print(f"{a} {w}")
else:
    print("вік повинен бути від 1 до 120")
