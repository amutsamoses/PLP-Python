# Program to calculate final price after applying discount if >= 20%

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it is 20% or higher.
    
    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.
        
    Returns:
        float: The final price after applying the discount (if >= 20%), 
               otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


if __name__ == "__main__":
    print("--- Discount Calculator ---")
    
    # Get user input for price and discount
    try:
        original_price = float(input("Enter the original price: "))
        discount = float(input("Enter the discount percentage: "))
        
        # Calculate final price using the function
        final_price = calculate_discount(original_price, discount)
        
        # Display the result
        if discount >= 20:
            print(f"Final price after discount: {final_price}")
        else:
            print(f"No discount applied. Final price: {final_price}")
            
    except ValueError:
        print("Invalid input! Please enter numeric values for price and discount.")