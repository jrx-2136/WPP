# Function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col, n):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):

    if row >= n:
        return True


    for col in range(n):
        if is_safe(board, row, col, n):

            board[row][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens(board, row + 1, n):
                return True


            board[row][col] = 0

    return False

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()

def eight_queens():
    n = 8  # Size of the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print_board(board, n)
    else:
        print("No solution exists")

if __name__ == "__main__":
    eight_queens()