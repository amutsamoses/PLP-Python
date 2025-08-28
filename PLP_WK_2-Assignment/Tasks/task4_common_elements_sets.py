
# Accepts two sets of integers from user and finds their common elements

# Get input for first set
set1 = set(map(int, input("Enter integers for the first set (separated by spaces): ").split()))

# Get input for second set
set2 = set(map(int, input("Enter integers for the second set (separated by spaces): ").split()))

# Find common elements
common_elements = set1 & set2

print(f"Common elements: {common_elements}")
