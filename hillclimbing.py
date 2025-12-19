import time

def neighbors_fn(x):
    return [x - 1, x + 1]

def value_fn(x):
    return -abs(x)

def hill_climbing(start):
    current = start
    iterations = 0
    evaluations = 0

    while True:
        iterations += 1
        neighbors = neighbors_fn(current)
        b = len(neighbors)

        best = current
        best_value = value_fn(current)
        evaluations += 1

        for n in neighbors:
            v = value_fn(n)
            evaluations += 1
            if v > best_value:
                best = n
                best_value = v

        if best == current:
            break

        current = best

    return current, iterations, evaluations, b


start = 10

t1 = time.perf_counter()
result, I, evals, b = hill_climbing(start)
t2 = time.perf_counter()

print("Result:", result)
print("Iterations (I):", I)
print("Branching Factor (b):", b)
print("Evaluations:", evals)
print("Execution Time:", t2 - t1)

print("\nEstimated Time Complexity:")
print(f"O({I} × {b}) ≈ O(I × b)")
