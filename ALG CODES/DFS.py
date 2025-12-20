import time

# ===============================
# INPUT
# ===============================
N = int(input("Enter number of queens (N): "))

if N == 2 or N == 3:
    print("❌ No solution exists for N =", N)
    exit()

# ===============================
# DRAW CHESSBOARD
# ===============================
def draw_board(board):
    print("\nChessboard Representation:\n")
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()

# ===============================
# DFS N-QUEENS
# ===============================
def n_queens_dfs(n):
    board = [-1] * n
    V = 0  # number of states visited
    E = 0  # number of edges tried

    def is_safe(row, col):
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True

    solutions_list = []

    def dfs(row):
        nonlocal V, E
        V += 1

        if row == n:
            # save one solution
            solutions_list.append(board.copy())
            return 1

        solutions = 0
        for col in range(n):
            E += 1
            if is_safe(row, col):
                board[row] = col
                solutions += dfs(row + 1)
                board[row] = -1
        return solutions

    total_solutions = dfs(0)
    return total_solutions, solutions_list, V, E

# ===============================
# MAIN
# ===============================
start_time = time.time()
total_solutions, solutions_list, V, E = n_queens_dfs(N)
end_time = time.time()
execution_time = end_time - start_time

# ===============================
# OUTPUT
# ===============================
print("\n==============================")
print(f"N = {N}")
print(f"Number of solutions found = {total_solutions}")
print(f"States visited (V) = {V}")
print(f"Edges tried (E) = {E}")
print(f"Time Complexity ≈ O(V + E) = {V + E}")
print(f"Execution Time = {round(execution_time, 6)} seconds")

# DRAW FIRST SOLUTION IF EXISTS
if total_solutions > 0:
    print("\nFirst solution:")
    draw_board(solutions_list[0])

print("==============================")
