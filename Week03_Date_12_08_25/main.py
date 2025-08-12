# Takes price and discount percentage and returns the discounted price
def calculate_discount(price, discount_percent) -> float:
    # If the discount is 20% or more, apply it
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        # If the discount is less than 20%, return the original price
        return price


def main():
    # Prompt user for inputs
    price = float(input("Enter the price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and print the discounted price
    discounted_price = calculate_discount(price, discount_percent)

    # Print the discounted price
    print(f"The discounted price is {discounted_price}")


if __name__ == "__main__":
    main()