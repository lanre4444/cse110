# Meal Price Calculator Project
# Creativity: I added a tip percentage option so customers can
# include a tip in their final bill before payment is calculated.

print("Welcome to Peace Restaurant!")
print("This calculator helps compute meals, taxes, tips, and customer change.\n")

# Ask for meal prices
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))

# Ask for number of people
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

# Calculate subtotal
subtotal = (child_price * children) + (adult_price * adults)

print(f"\nSubtotal: ${subtotal:.2f}")

# Ask for sales tax
tax_rate = float(input("\nWhat is the sales tax rate? "))

# Calculate tax
sales_tax = subtotal * (tax_rate / 100)

# Creativity addition: tip percentage
tip_rate = float(input("What tip percentage would you like to give? "))

tip_amount = subtotal * (tip_rate / 100)

# Calculate total
total = subtotal + sales_tax + tip_amount

print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Tip: ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")

# Payment
payment = float(input("\nWhat is the payment amount? "))

change = payment - total

print(f"Change: ${change:.2f}")