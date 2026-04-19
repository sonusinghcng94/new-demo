# ================================================================
#           HOSPITAL PATIENT BILLING SYSTEM
# ================================================================
# Rules:
#   Child discount   : age < 12  → 50% off consultation fee
#   High-bill discount: total > 5000 → 10% off total
#   Senior discount  : age >= 60 → 5% off total
#   Service tax      : after-discount total > 7000 → 5% tax
# ================================================================


# ── Helper: validated input functions ───────────────────────────

def get_name():
    """Accept a non-empty name containing at least one letter."""
    while True:
        name = input("  Patient Name        : ").strip()
        if not name:
            print("  [Error] Name cannot be empty.\n")
        elif not any(c.isalpha() for c in name):
            print("  [Error] Name must contain at least one letter.\n")
        else:
            return name

def get_age():
    """Accept an integer age between 0 and 120 (inclusive)."""
    while True:
        try:
            age = int(input("  Age (years)         : "))
            if age < 0 or age > 120:
                print("  [Error] Age must be between 0 and 120.\n")
            else:
                return age
        except ValueError:
            print("  [Error] Please enter a whole number for age.\n")

def get_fee(label):
    """Accept a non-negative float for any fee."""
    while True:
        try:
            value = float(input(f"  {label:<20}: AED "))
            if value < 0:
                print("  [Error] Fee cannot be negative.\n")
            else:
                return value
        except ValueError:
            print("  [Error] Please enter a valid number.\n")


# ── Step 1 & 2: Collect and validate inputs ──────────────────────

print("=" * 55)
print("         HOSPITAL PATIENT BILLING SYSTEM")
print("=" * 55)
print("  Please enter patient details:\n")

name             = get_name()
age              = get_age()
consultation_fee = get_fee("Consultation Fee")
lab_charges      = get_fee("Lab Charges")
medicine_charges = get_fee("Medicine Charges")


# ── Step 3: Calculate bill ───────────────────────────────────────

# 3a. Total before any discount
total_before_discount = consultation_fee + lab_charges + medicine_charges

# 3b. Child discount: 50% off consultation if age < 12
child_discount = 0.0
if age < 12:
    child_discount = consultation_fee * 0.50

# Adjusted total after child discount (only consultation reduced)
adjusted_total = (consultation_fee - child_discount) + lab_charges + medicine_charges

# 3c. High-bill discount: 10% off if adjusted total > 5000
high_bill_discount = 0.0
if adjusted_total > 5000:
    high_bill_discount = adjusted_total * 0.10

# 3d. Senior discount: 5% off if age >= 60
senior_discount = 0.0
if age >= 60:
    senior_discount = adjusted_total * 0.05

# 3e. Total discount and amount after all discounts
total_discount  = child_discount + high_bill_discount + senior_discount
after_discount  = total_before_discount - total_discount

# 3f. Service tax: 5% if after-discount total > 7000
service_tax = 0.0
if after_discount > 7000:
    service_tax = after_discount * 0.05

# 3g. Final payable
final_payable = after_discount + service_tax


# ── Step 4: Display final bill ───────────────────────────────────

W = 55
print("\n" + "=" * W)
print("              PATIENT BILL RECEIPT")
print("=" * W)

# Patient info
print(f"  Patient Name         : {name}")
age_tag = ""
if age < 12:
    age_tag = " (Child)"
elif age >= 60:
    age_tag = " (Senior Citizen)"
print(f"  Age                  : {age}{age_tag}")
print("-" * W)

# Charge breakdown
print(f"  {'Consultation Fee':<25} AED {consultation_fee:>9.2f}")
print(f"  {'Lab Charges':<25} AED {lab_charges:>9.2f}")
print(f"  {'Medicine Charges':<25} AED {medicine_charges:>9.2f}")
print("-" * W)
print(f"  {'Total Before Discount':<25} AED {total_before_discount:>9.2f}")
print("-" * W)

# Discounts (only show applicable ones)
if child_discount > 0:
    print(f"  {'Child Discount (50%)':<25} AED {-child_discount:>9.2f}")
if high_bill_discount > 0:
    print(f"  {'High-Bill Disc (10%)':<25} AED {-high_bill_discount:>9.2f}")
if senior_discount > 0:
    print(f"  {'Senior Discount (5%)':<25} AED {-senior_discount:>9.2f}")

print(f"  {'Total Discount':<25} AED {-total_discount:>9.2f}")
print("-" * W)
print(f"  {'Amount After Discount':<25} AED {after_discount:>9.2f}")

# Tax (only show if applicable)
if service_tax > 0:
    print(f"  {'Service Tax (5%)':<25} AED {service_tax:>9.2f}")
else:
    print(f"  {'Service Tax':<25}        None")

print("=" * W)
print(f"  {'FINAL PAYABLE AMOUNT':<25} AED {final_payable:>9.2f}")
print("=" * W)