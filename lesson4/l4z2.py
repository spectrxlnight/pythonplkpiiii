def decreasing(num):
    s = str(num)
    for i in range(len(s) - 1):
        if s[i] <= s[i + 1]:
            return False
    return True
def divisible_by_3(num):
    return sum(map(int, str(num))) % 3 == 0
passwords = []
for n in range(1000000, 10000000):
    if decreasing(n) and divisible_by_3(n):
        passwords.append(n)
print("правильні паролі:", len(passwords))
print("приклади ", passwords[:10])  
p = input("пароль: ")
if len(p) == 7 and p.isdigit():
    n = int(p)
    if decreasing(n) and divisible_by_3(n):
        print("так!")
    else:
        print("ні!")
else:
    print("не 7((((((!")
