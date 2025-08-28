# Week 3 Assignment

## 📄 Description

This week's task focuses on **functions**, **conditional logic**, and **user input handling** in Python.  
The goal is to create a function that calculates the final price of an item after applying a discount, with a condition that only applies the discount if it is **20% or higher**.

---

## **Objectives**

- Practice defining and using functions in Python.
- Use `if` statements to implement conditional logic.
- Collect and process user input.

---

## **Task Requirements**

1. Create a function named **`calculate_discount(price, discount_percent)`**:
   - Takes two parameters: the original price and the discount percentage.
   - Returns the price after applying the discount **only if the discount is 20% or higher**.
   - Returns the original price if the discount is **less than 20%**.

2. Prompt the user to:
   - Enter the original price.
   - Enter the discount percentage.
   - Print the final price after applying the discount logic.

---

## **Example Run**

```text
Enter the original price: 1000
Enter the discount percentage: 25
Final price after discount: 750.0
text
Copy code
Enter the original price: 1000
Enter the discount percentage: 15
No discount applied. Final price: 1000.0
File Name
Copy code
week3_discount_calculator.py
How to Run
Open your terminal in the project directory and run:

bash
Copy code
python week3_discount_calculator.py