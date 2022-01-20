from re import L


class QueensProb:
    def __init__(self, n):
        self.n = n
        self.chess_board = [[None for i in range(n)]for j in range(n)]

    def Solve_problem(self):
        # We solve using an external function, starting from index '0':
        if self.solve(0):
            return self.Print()
        else:
            # After considering all possible solutions without any success
            print("There's no soltution")

    def solve(self, col_index):
        # Checking for the base case
        if col_index == self.n:
            return True

        # Try to find out a position for the queen in a given column:
        for row_index in range(self.n):
            if self.is_valid_place(row_index, col_index):
                # 1 means there is queen at the given index
                self.chess_board[row_index][col_index] = 1

                # Try to find a safe position for the queen in next column
                if self.solve(col_index+1):
                    return True

                # Otherwise, BACKTRACK:
                self.chess_board[row_index][col_index] = 0
        # When we have considered all rows and columns without any success:
        return False

    def is_valid_place(self, row_index, col_index):
        # Check if the queens can attack each other horizontally:
        for i in range(self.n):
            if self.chess_board[row_index][i] == 1:
                return False
        # No need to check for columns:

        # Check for diagonals:
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break

            if self.chess_board[i][j] == 1:
                return False

            j = j-1

        # Check for diagonals:
        j = col_index
        for i in range(row_index, self.n):
            if j < 0:
                break

            if self.chess_board[i][j] == 1:
                return False

            j = j-1

        return True

    def Print(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_board[i][j] == 1:
                    print(' Q ', end='')
                else:
                    print(' - ', end='')
            print('\n')


if __name__ == '__main__':
    Object = QueensProb(4)
    Object.Solve_problem()
    # Object.Print()
