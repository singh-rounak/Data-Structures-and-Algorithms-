
class solution:

    def fact(self, n):
        if n == 1:
            return 1

        res = self.fact(n-1)
        return n*res

    def FactTail(self, n, accumulator=1):
        if n == 1:
            return accumulator

        return self.FactTail(n-1, n*accumulator)


print(solution().fact(10))
print(solution().FactTail(10))
print(repr(solution()))
