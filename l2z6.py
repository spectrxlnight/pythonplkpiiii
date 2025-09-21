fib = [0] * 12  
if len(fib) > 0:
    fib[0] = 0
if len(fib) > 1:
    fib[1] = 1
for i in range(2, 12):
    fib[i] = fib[i-1] + fib[i-2]
print(fib)
