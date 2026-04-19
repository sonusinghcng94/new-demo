# ============================================================
#        CLASS ACTIVITY 1 – Final Movie Ticket Cost
# ============================================================
# Rules:
#   - Price per ticket : AED 35
#   - Tickets >= 5     : 10% discount on total amount
# ============================================================

PRICE_PER_TICKET = 35.0
DISCOUNT_RATE    = 0.10
DISCOUNT_MIN     = 5

# ── Step 1: Input & Validation ───────────────────────────────
print("=" * 45)
print("       CINEMA TICKET COST CALCULATOR")
print("=" * 45)

while True:
    try:
        num_tickets = int(input("  Enter number of tickets: "))
        if num_tickets <= 0:
            print("  [Error] Number of tickets must be greater than 0.")
        else:
            break
    except ValueError:
        print("  [Error] Invalid input. Please enter a whole number.")

# ── Step 2: Calculate Total Cost ────────────────────────────
total_cost = num_tickets * PRICE_PER_TICKET

# ── Step 3: Apply Discount if Applicable ────────────────────
discount = 0.0
if num_tickets >= DISCOUNT_MIN:
    discount = total_cost * DISCOUNT_RATE

final_amount = total_cost - discount

# ── Step 4: Display Final Bill ───────────────────────────────
print("\n" + "-" * 45)
print(f"  Price per Ticket   : AED {PRICE_PER_TICKET:.2f}")
print(f"  Number of Tickets  : {num_tickets}")
print(f"  Total Cost         : AED {total_cost:.2f}")

if discount > 0:
    print(f"  Discount (10%)     : AED -{discount:.2f}")
    print(f"  [5 or more tickets — discount applied!]")
else:
    print(f"  Discount           : None")

print("-" * 45)
print(f"  FINAL AMOUNT       : AED {final_amount:.2f}")
print("=" * 45)