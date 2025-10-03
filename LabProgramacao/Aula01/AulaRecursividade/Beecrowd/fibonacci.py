func = -1
def fibonacci(a: int):
    global func 
    func = func+1
    if a == 0: return 0
    if a == 1: return 1
    return fibonacci(a-1) + fibonacci(a-2)

i = int(input())
for j in range(i):
    a = int(input())
    {fibonacci(a)}
    print(f"fib({a}) = {func} calls = {fibonacci(a)}")
    func = -1