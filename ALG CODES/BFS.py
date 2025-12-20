from collections import deque
import time

# ===============================
# INPUT
# ===============================
N = int(input("Enter number of queens (N): "))

if N == 2 or N == 3:
    print("❌ No solution exists for N =", N)
    exit()

# ===============================
# CHECK IF SAFE
# ===============================
def is_safe(state, row, col):
    for r in range(row):
        c = state[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

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
# BFS N-QUEENS
# ===============================
def bfs_n_queens(n):
    queue = deque()
    queue.append([])

    while queue:
        state = queue.popleft()
        row = len(state)

        if row == n:
            return state

        for col in range(n):
            if is_safe(state, row, col):
                queue.append(state + [col])
    return None

# ===============================
# MAIN
# ===============================
start_time = time.time()
solution = bfs_n_queens(N)
end_time = time.time()

# ===============================
# TIME COMPLEXITY ESTIMATION
# ===============================
# Approximate number of operations:
# In BFS, each state generates up to N children, worst case ~O(N!)
# We'll estimate roughly: total_nodes * N²
# Here we approximate total_nodes = number of nodes generated ≈ len(solution) factorial (rough approx)
if solution:
    total_nodes_estimate = 1
    for i in range(1, N+1):
        total_nodes_estimate *= i  # N!
else:
    total_nodes_estimate = 0

execution_time = end_time - start_time

# ===============================
# OUTPUT
# ===============================
print("\n==============================")

if solution:
    print("✅ Solution Found!")
    print("Board Representation (column : row):")
    print(solution)
else:
    print("❌ No solution found.")

# DRAW BOARD
if solution:
    draw_board(solution)

print("\nExecution Details:")
print("Execution Time:", round(execution_time, 6), "seconds")

print("\nTime Complexity Analysis (Estimated):")
print("Theoretical Worst-Case: O(N!)")
print(f"Estimated Nodes Generated ≈ {total_nodes_estimate}")
print("==============================")
