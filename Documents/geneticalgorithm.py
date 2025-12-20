import random
import time

# ===============================
# INPUT
# ===============================
N = int(input("Enter number of queens (N): "))

if N == 2 or N == 3:
    print("❌ No solution exists for N =", N)
    exit()

# ===============================
# PARAMETERS
# ===============================
POP_SIZE = 100
MAX_GENERATIONS = 3000
MUTATION_RATE = 0.1
ELITISM = 2

# ===============================
# GA FUNCTIONS
# ===============================

def generate_chromosome():
    return [random.randint(0, N - 1) for _ in range(N)]


def fitness(chromosome):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if chromosome[i] == chromosome[j] or \
               abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def selection(population):
    a, b = random.sample(population, 2)
    return a if fitness(a) < fitness(b) else b


def crossover(parent1, parent2):
    point = random.randint(1, N - 2)
    return parent1[:point] + parent2[point:]


def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, N - 1)
        chromosome[index] = random.randint(0, N - 1)


# ===============================
# DRAW CHESSBOARD (ADDED ONLY)
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
# MAIN ALGORITHM
# ===============================
population = [generate_chromosome() for _ in range(POP_SIZE)]
solution = None
generation = 0

start_time = time.time()

while generation < MAX_GENERATIONS:
    population.sort(key=lambda x: fitness(x))

    if fitness(population[0]) == 0:
        solution = population[0]
        break

    new_population = population[:ELITISM]

    while len(new_population) < POP_SIZE:
        p1 = selection(population)
        p2 = selection(population)
        child = crossover(p1, p2)
        mutate(child)
        new_population.append(child)

    population = new_population
    generation += 1

end_time = time.time()

# ===============================
# TIME COMPLEXITY CALCULATION
# ===============================
execution_time = end_time - start_time
time_complexity_ops = POP_SIZE * generation * (N ** 2)
ops_per_second = time_complexity_ops / execution_time if execution_time > 0 else 0

# ===============================
# OUTPUT
# ===============================
print("\n==============================")

if solution:
    print("✅ Solution Found!")
    print("Board Representation (column : row):")
    print(solution)
    print("Fitness:", fitness(solution))

    # DRAW BOARD (ONLY ADDITION)
    draw_board(solution)

else:
    print("❌ No solution found.")

print("\nExecution Details:")
print("Generations:", generation)
print("Execution Time:", round(execution_time, 6), "seconds")

print("\nTime Complexity Analysis:")
print("Theoretical Formula: O(P × G × N²)")
print(f"T(N) = {POP_SIZE} × {generation} × {N}²")
print(f"T(N) = {time_complexity_ops:,} operations")

print("\nPerformance Estimation:")
print(f"Operations per second ≈ {int(ops_per_second):,}")

print("==============================")
