import random
import time

# =============================
# Fitness Function
# =============================
def fitness(board):
    """
    Counts number of attacking pairs of queens.
    Goal: fitness = 0
    """
    attacks = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks


# =============================
# Generate Neighbors
# =============================
def get_neighbors(board):
    """
    Generate all neighbors by moving one queen in its column
    """
    neighbors = []
    n = len(board)

    for col in range(n):
        for row in range(n):
            if row != board[col]:
                neighbor = board.copy()
                neighbor[col] = row
                neighbors.append(neighbor)

    return neighbors


# =============================
# Draw Chessboard (ASCII)
# =============================
def draw_board(board):
    n = len(board)
    print("\nChessboard Representation:\n")

    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


# =============================
# Hill Climbing Algorithm
# =============================
def hill_climbing(n, max_steps=1000):
    # Random initial state
    current = [random.randint(0, n - 1) for _ in range(n)]
    current_fitness = fitness(current)

    steps = 0
    evaluations = 1  # initial evaluation
    b = n * (n - 1)  # branching factor

    while steps < max_steps and current_fitness != 0:
        steps += 1
        neighbors = get_neighbors(current)

        best = current
        best_fitness = current_fitness

        for neighbor in neighbors:
            f = fitness(neighbor)
            evaluations += 1
            if f < best_fitness:
                best = neighbor
                best_fitness = f

        if best_fitness >= current_fitness:
            break  # Local optimum reached

        current = best
        current_fitness = best_fitness

    return current, current_fitness, steps, evaluations, b


# =============================
# Main
# =============================
if __name__ == "__main__":
    n = int(input("Enter number of queens (N): "))

    start_time = time.perf_counter()
    solution, fit, steps, evals, b = hill_climbing(n)
    end_time = time.perf_counter()

    print("\n==============================")
    if fit == 0:
        print("✅ Solution Found!")
    else:
        print("⚠️ Local Optimum Reached (Not Optimal)")

    print("Board Representation (column : row):")
    print(solution)
    print("Fitness:", fit)

    # 🔹 Draw the chessboard
    draw_board(solution)

    print("\nExecution Details:")
    print("Iterations (I):", steps)
    print("Branching Factor (b):", b)
    print("Evaluations:", evals)
    print("Execution Time:", end_time - start_time)

    # =============================
    # Time Complexity Calculation
    # =============================
    print("\nTime Complexity Analysis:")
    print("Theoretical Big-O: O(I × N²)")
    print(f"T(N) ≈ {steps} × {n}² = {steps * n * n} operations")
    print("==============================")
