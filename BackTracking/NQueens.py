from re import L


class Queens:
    def __init__(self, n):
        self.n = n
        self.board = [[None for i in range(n)]for j in range(n)]

    def Print(self):
        print(self.board)

    def Solve_problem(self):
        if self.solve(0):
            return self.print(0)
        else:
            print("There's no soltution")


if __name__ == '__main__':
    Object = Queens(4)
    Object.Print()
