import random
lst = [random.randint(0, 99) for _ in range(10)]
total_sum = sum(lst)
print("Список:", lst)
print("Сума:", total_sum)