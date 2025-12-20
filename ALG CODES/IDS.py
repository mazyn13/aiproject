import time

# ===============================
# INPUT
# ===============================
N = int(input("Enter number of queens (N): "))

if N == 2 or N == 3:
    print("❌ No solution exists for N =", N)
    exit()

# ===============================
# FITNESS FUNCTION
# ===============================
def fitness(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# ===============================
# DRAW BOARD
# ===============================
def draw_board(board):
    print("\nChessboard:")
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()
    print()

# ===============================
# SAFETY CHECK
# ===============================
def is_safe(board, row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

# ===============================
# DEPTH LIMITED DFS
# ===============================
def depth_limited_dfs(board, row, limit, counters):
    counters["nodes"] += 1

    if row == N:
        return board

    if row >= limit:
        return None

    for col in range(N):
        counters["edges"] += 1
        if is_safe(board, row, col):
            board[row] = col
            result = depth_limited_dfs(board, row + 1, limit, counters)
            if result:
                return result
            board[row] = -1

    return None

# ===============================
# ITERATIVE DEEPENING SEARCH
# ===============================
start_time = time.time()

solution = None
depth = 0
total_nodes = 0
total_edges = 0

while depth <= N:
    board = [-1] * N
    counters = {"nodes": 0, "edges": 0}

    result = depth_limited_dfs(board, 0, depth, counters)

    total_nodes += counters["nodes"]
    total_edges += counters["edges"]

    if result:
        solution = result
        break

    depth += 1

end_time = time.time()

# ===============================
# TIME COMPLEXITY
# ===============================
execution_time = end_time - start_time
estimated_ops = total_nodes + total_edges

# ===============================
# OUTPUT
# ===============================
print("\n==============================")

if solution:
    print("✅ Solution Found!")
    print("Board Representation (column : row):")
    print(solution)
    print("Fitness:", fitness(solution))
    draw_board(solution)
else:
    print("❌ No solution found.")

print("\nExecution Details:")
print("Max Depth Reached:", depth)
print("States Visited (V):", total_nodes)
print("Edges Tried (E):", total_edges)
print("Execution Time:", round(execution_time, 6), "seconds")

print("\nTime Complexity Analysis:")
print("Theoretical Big-O: O(b^d)")
print("Estimated Operations ≈ V + E =", estimated_ops)

print("==============================")
