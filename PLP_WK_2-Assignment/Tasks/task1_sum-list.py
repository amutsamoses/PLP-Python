
# Accepts user input to create a list of integers and computes their sum

# Ask user for a list of numbers separated by spaces
numbers = input("Enter integers separated by spaces: ")

# Convert input to a list of integers
int_list = [int(num) for num in numbers.split()]

# Calculate the sum
total_sum = sum(int_list)

print(f"The sum of the integers is: {total_sum}")
