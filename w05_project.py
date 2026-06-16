# Shopping Cart Program
# Creativity: I added a feature that displays the number of items
# currently in the shopping cart whenever the cart is viewed.

print("Welcome to the Shopping Cart Program!")

items = []
prices = []

action = 0

while action != 5:

    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = int(input("Please enter an action: "))

    # ADD ITEM
    if action == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))

        items.append(item)
        prices.append(price)

        print(f"'{item}' has been added to the cart.")

    # VIEW CART
    elif action == 2:
        print("The contents of the shopping cart are:")

        for i in range(len(items)):
            print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")

        print(f"\nTotal items in cart: {len(items)}")

    # REMOVE ITEM
    elif action == 3:

        print("The contents of the shopping cart are:")

        for i in range(len(items)):
            print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")

        remove_number = int(
            input("\nWhich item would you like to remove? ")
        )

        remove_index = remove_number - 1

        if 0 <= remove_index < len(items):
            items.pop(remove_index)
            prices.pop(remove_index)
            print("Item removed.")
        else:
            print("Sorry, that is not a valid item number.")

    # COMPUTE TOTAL
    elif action == 4:

        total = 0

        for price in prices:
            total += price

        print(
            f"The total price of the items in the shopping cart is ${total:.2f}"
        )

    # QUIT
    elif action == 5:
        print("Thank you. Goodbye.")

    else:
        print("Please enter a valid option.")