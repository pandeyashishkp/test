def fib(a):
    if a == 1 or a == 0:
        return 1
    else:
        return(fib(a-1) + fib(a-2))

for i in range(5):
    print(fib(i))
