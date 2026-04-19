# ============================================================
#          PRACTICE PROBLEM 2 – Electricity Bill Calculator
# ============================================================
# Slab rates:
#   0  – 100  units  →  AED 0.50 per unit
#   101– 300  units  →  AED 0.75 per unit
#   301– 500  units  →  AED 1.20 per unit
#   500+      units  →  AED 1.50 per unit
# ============================================================

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  [Error] Units cannot be negative.")
            else:
                return value
        except ValueError:
            print("  [Error] Please enter a valid number.")

print("=" * 45)
print("      ELECTRICITY BILL CALCULATOR")
print("=" * 45)

units = get_positive_float("  Units Consumed : ")

if units <= 100:
    bill = units * 0.50
    rate = "AED 0.50/unit"
elif units <= 300:
    bill = units * 0.75
    rate = "AED 0.75/unit"
elif units <= 500:
    bill = units * 1.20
    rate = "AED 1.20/unit"
else:
    bill = units * 1.50
    rate = "AED 1.50/unit"

print("\n" + "-" * 45)
print(f"  Units Consumed : {units}")
print(f"  Rate Applied   : {rate}")
print(f"  Total Bill     : AED {bill:.2f}")
print("=" * 45)