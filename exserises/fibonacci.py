def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

def fib_li(num):
    a = 0
    b = 1
    li = []
    for i in range(num):
        li.append(a)
        temp = a
        a = b
        b = temp + b
    return li

fibonacci = fib(20)
for i in range(20):
    print(next(fibonacci))
print(fib_li(20))