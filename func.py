def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, apply the discount; otherwise, return the original price.
    
    :param price: float - The original price of the item.
    :param discount_percent: float - The discount percentage.
    :return: float - The final price after applying the discount if applicable.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price

# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Final price after discount: ${round(final_price, 2)}")
else:
    print(f"No discount applied. Original price: ${round(price, 2)}")
