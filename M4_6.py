import random

n = int(input("How many random points should we generate? "))

inside = 0

for _ in range(n):
    x, y = random.uniform(-1,1),random.uniform(-1,1)
    if x*2 + y*2 <= 1:
        inside += 1
pi_approx = 4 * inside / n
print(f"Approximaton of pi: {pi_approx}")