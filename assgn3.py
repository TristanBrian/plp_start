def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    
    Returns:
    float: The final price after applying the discount, or the original price if no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Main function to test the calculate_discount function
# Print the final price after applying the discount, or if no discount was applied, print the original price
def main():
    try:
        price = float(input("Enter the original price of the item: Ksh "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(price, discount_percent)
        
        print(f"\nOriginal Price: Ksh {price:.2f}")
        print(f"Discount Percentage: {discount_percent}%")
        if discount_percent >= 20:
            print(f"Final Price after {discount_percent}% discount: Ksh {final_price:.2f}")
        else:
            print(f"No discount applied. Price remains: Ksh {final_price:.2f}")
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage")

if __name__ == "__main__":
    main()
    
