# Function to check if base raised to exponent is greater than 5000

def large_power(base, exponent):
    """
    Returns True if base raised to the power of exponent is greater than 5000.
    Otherwise, returns False.

    Args:
        base (int or float): The base number.
        exponent (int): The exponent.

    Returns:
        bool: True if base**exponent > 5000, else False.
    """
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False


# Example usage:
if __name__ == "__main__":
    print("Testing large_power() function:")
    print(f"large_power(2, 12) → {large_power(2, 12)}")  # False (4096)
    print(f"large_power(10, 4) → {large_power(10, 4)}")  # True (10000)