import random  

# Generate 100 random numbers between 0 and 10
num = [random.randint(0, 10) for _ in range(100)]

# Generate 10 random query numbers between 0 and 12
queries = [random.randint(0, 12) for _ in range(10)]

# Create a frequency array of size 11 (for numbers 0–10)
freq = [0] * 11

# This list will store the final answers
result = []

# Step 1: Count frequency of each number in 'num'
for n in num:
    freq[n] += 1   # increase count at index = number

# Step 2: Process each query
for q in queries:
    
    # If query is outside valid range (0–10)
    if q < 0 or q > 10:
        print(f"{q} not found in num list")
        result.append(0)   # optional: keep result size consistent
    
    else:
        # Append frequency of that number
        result.append(freq[q])

# Final output: frequency results for all queries
print("Queries:", queries)
print("Frequencies:", result)
