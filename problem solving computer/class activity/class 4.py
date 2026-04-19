# ============================================================
#          MAIN PROBLEM – Cinema Ticket Total Calculator
# ============================================================
# Ticket Prices:
#   Adult  (age 13–59) → AED 40
#   Child  (age 0–12)  → AED 20
#   Senior (age 60+)   → AED 25
#
# Rules:
#   - Groups of 5 or more → 10% group discount
#   - Concession (popcorn/drinks) can be added per ticket
#   - 5% service tax on final total
# ============================================================

ADULT_PRICE  = 40.0
CHILD_PRICE  = 20.0
SENIOR_PRICE = 25.0
GROUP_MIN    = 5
GROUP_DISC   = 0.10
SERVICE_TAX  = 0.05

def get_int(prompt, min_val=0):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"  [Error] Value must be at least {min_val}.")
            else:
                return value
        except ValueError:
            print("  [Error] Please enter a whole number.")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  [Error] Amount cannot be negative.")
            else:
                return value
        except ValueError:
            print("  [Error] Please enter a valid number.")

print("=" * 50)
print("       CINEMA TICKET TOTAL CALCULATOR")
print("=" * 50)
print(f"  Adult ticket  : AED {ADULT_PRICE:.2f}")
print(f"  Child ticket  : AED {CHILD_PRICE:.2f}  (age ≤ 12)")
print(f"  Senior ticket : AED {SENIOR_PRICE:.2f}  (age ≥ 60)")
print(f"  Group discount: 10% for {GROUP_MIN}+ tickets")
print(f"  Service tax   : 5%")
print("-" * 50)

num_adults  = get_int("  Number of Adults  : ", min_val=0)
num_children = get_int("  Number of Children: ", min_val=0)
num_seniors = get_int("  Number of Seniors : ", min_val=0)

total_tickets = num_adults + num_children + num_seniors

if total_tickets == 0:
    print("\n  [Error] Please enter at least one ticket.")
else:
    concession = get_float("  Concession per ticket (AED, 0 if none): ")

    # ── Calculate ──────────────────────────────────────────
    adult_cost   = num_adults   * ADULT_PRICE
    child_cost   = num_children * CHILD_PRICE
    senior_cost  = num_seniors  * SENIOR_PRICE
    concession_total = concession * total_tickets

    subtotal     = adult_cost + child_cost + senior_cost + concession_total

    group_discount = 0.0
    if total_tickets >= GROUP_MIN:
        group_discount = subtotal * GROUP_DISC

    after_discount = subtotal - group_discount
    tax            = after_discount * SERVICE_TAX
    final_total    = after_discount + tax

    # ── Display receipt ────────────────────────────────────
    print("\n" + "=" * 50)
    print("              CINEMA RECEIPT")
    print("=" * 50)
    if num_adults > 0:
        print(f"  Adults  : {num_adults} x AED {ADULT_PRICE:.2f}  = AED {adult_cost:.2f}")
    if num_children > 0:
        print(f"  Children: {num_children} x AED {CHILD_PRICE:.2f}  = AED {child_cost:.2f}")
    if num_seniors > 0:
        print(f"  Seniors : {num_seniors} x AED {SENIOR_PRICE:.2f}  = AED {senior_cost:.2f}")
    if concession > 0:
        print(f"  Concession: {total_tickets} x AED {concession:.2f} = AED {concession_total:.2f}")
    print("-" * 50)
    print(f"  {'Subtotal':<30} AED {subtotal:.2f}")
    if group_discount > 0:
        print(f"  {'Group Discount (10%)':<30} AED -{group_discount:.2f}")
    print(f"  {'Service Tax (5%)':<30} AED +{tax:.2f}")
    print("=" * 50)
    print(f"  {'TOTAL PAYABLE':<30} AED {final_total:.2f}")
    print("=" * 50)
    print(f"  Total tickets: {total_tickets}" + 
          ("  [Group discount applied]" if group_discount > 0 else ""))
    print("=" * 50)