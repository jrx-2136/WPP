import numpy as np

# Create a sample numpy array
arr = np.array(["apple", "banana", "cherry", "date", "elderberry"])

# Make each element 15 characters long and apply different justifications
centered = np.array([s.center(15, '_') for s in arr])
left_justified = np.array([s.ljust(15, '_') for s in arr])
right_justified = np.array([s.rjust(15, '_') for s in arr])

# Print the results
print("Original Array:")
print(arr)
print("\nCentered:")
print(centered)
print("\nLeft-Justified:")
print(left_justified)
print("\nRight-Justified:")
print(right_justified)