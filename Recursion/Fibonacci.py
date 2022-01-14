
"""          METHOD 1:  Backtracking (Head Recursion)
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

# This method has two recursive calls - values are calculated Twice
    res1 = fib(n-2)
    res2 = fib(n-1)
    return res1 + res2


for i in range(10):
    print(fib(i))


"""             METHOD 2: Dynamic Proogramming (Tail Recursion)
"""


def fibm2(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b

    return fibm2(n-1, b, a+b)


print(fibm2(3))
