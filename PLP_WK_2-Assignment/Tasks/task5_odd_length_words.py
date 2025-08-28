
# Filters words with odd character lengths from a list using list comprehension

# List of words
words = ["apple", "banana", "cherry", "date", "fig", "grape"]

# List comprehension to filter words with odd lengths
odd_length_words = [word for word in words if len(word) % 2 != 0]

print(f"Words with odd number of characters: {odd_length_words}")
