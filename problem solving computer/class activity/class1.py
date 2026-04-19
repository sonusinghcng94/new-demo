# Movie Ticket Cost Calculator

TICKET_PRICE = 35  # AED per ticket

# Input values 
tickets = int(input("Enter number of tickets: "))

# Validation
if tickets <= 0:
    print("Number of tickets must be greater than 0!")
else:
    # Calculate total cost
    total_cost = tickets * TICKET_PRICE

    # Apply discount if applicable
    if tickets >= 5:
        discount = 0.10 * total_cost
    else:
        discount = 0

    final_amount = total_cost - discount

    # Output
    print("\n----- Movie Ticket Bill -----")
    print("Number of Tickets:", tickets)
    print("Total Cost:", total_cost, "AED")
    print("Discount:", discount, "AED")
    print("Final Amount:", final_amount, "AED")