import random

# Generate and print 10 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(10)]
print(' '.join(map(str, numbers)))