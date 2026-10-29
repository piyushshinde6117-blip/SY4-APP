
import pandas as pd
import random

# Create a Series of 10 random numbers
numbers = [random.randint(1, 100) for i in range(10)]
s = pd.Series(numbers)

print("Series:")
print(s)

# Indexing
print("\nElement at index 2:")
print(s[2])

# Filtering: numbers greater than 50
print("\nNumbers greater than 50:")
print(s[s > 50])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())