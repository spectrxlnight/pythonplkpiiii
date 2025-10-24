x, y = map(float, input("Введіть координати точки (x y): ").split())
if x > 0 and y > 0:
    print("точка знаходиться в 1 чверті")
elif x < 0 and y > 0:
    print("точка знаходиться в 2 чверті")
elif x < 0 and y < 0:
    print("точка знаходиться в 3 чверті")
elif x > 0 and y < 0:
    print("точка знаходиться в 4 чверті")
