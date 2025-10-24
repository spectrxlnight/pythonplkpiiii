def db(n):
    if n == 0:
        return "0"
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n //= 2
    return b
def bd(b):
    dec = 0
    for digit in b:
        dec = dec * 2 + int(digit)
    return dec
print("оберіть дію:")
print("1 - перетворити з десяткової у двійкову")
print("2 - перетворити з двійкової у десяткову")
choice = input("вибір (1/2): ")
if choice == "1":
    n = int(input("Введіть десяткове число: "))
    print("у двійковій системі:", db(n))
elif choice == "2":
    b = input("Введіть двійкове число: ")
    print("у десятковій системі:", bd(b))
else:
    print("неправильний вибір!")
