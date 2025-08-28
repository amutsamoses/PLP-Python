# Function to check if a number is divisible by ten

def divisible_by_ten(num):
    """
    Returns True if the given number is divisible by 10.
    Otherwise, returns False.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if num is divisible by 10, else False.
    """
    if num % 10 == 0:
        return True
    else:
        return False


# Example usage:
if __name__ == "__main__":
    print("Testing divisible_by_ten() function:")
    print(f"divisible_by_ten(100) → {divisible_by_ten(100)}")  # True
    print(f"divisible_by_ten(33) → {divisible_by_ten(33)}")    # False
    print(f"divisible_by_ten(50) → {divisible_by_ten(50)}")    # True