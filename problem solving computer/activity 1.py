# Movie Ticket Cost Calculator

# Step 1: Ask user for number of tickets
tickets = int(input("Enter number of tickets: "))

# Step 2: Validate input
if tickets <= 0:
    print("Invalid input. Number of tickets must be greater than 0.")
else:
    price_per_ticket = 35

    # Step 3: Calculate total cost
    total_cost = tickets * price_per_ticket

    # Step 4: Apply discount if applicable
    if tickets >= 5:
        discount = total_cost * 0.10
        final_amount = total_cost - discount
    else:
        final_amount = total_cost

    # Step 5: Display final amount
    print("Total cost:", total_cost, "AED")
    if tickets >= 5:
        print("Discount applied: 10%")
    print("Final amount to pay:", final_amount, "AED")