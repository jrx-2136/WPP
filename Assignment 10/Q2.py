import random

def is_safe(board, row, col, n):
    # Check this row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = 0  

    return False

def generate_random_solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    while not solve_n_queens(board, 0, n):
        board = [[0 for _ in range(n)] for _ in range(n)]
    return board

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

if __name__ == "__main__":
    n = 8  # Size of the chessboard (8x8 for standard N-Queens)
    solution = generate_random_solution(n)
    print("One of the solutions to the N-Queens problem:")
    print_board(solution)