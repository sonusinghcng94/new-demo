# ============================================================
#          PRACTICE PROBLEM 3 – Savings Program with 5% Tax
# ============================================================

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  [Error] Amount cannot be negative.")
            else:
                return value
        except ValueError:
            print("  [Error] Please enter a valid number.")

print("=" * 45)
print("       SAVINGS CALCULATOR WITH TAX")
print("=" * 45)

income   = get_positive_float("  Monthly Income   : AED ")
expenses = get_positive_float("  Monthly Expenses : AED ")

if expenses > income:
    print("\n  [Warning] Expenses exceed income — no savings!")
else:
    savings        = income - expenses
    tax            = savings * 0.05       # 5% tax on savings
    savings_after_tax = savings - tax

    print("\n" + "-" * 45)
    print(f"  Monthly Income      : AED {income:.2f}")
    print(f"  Monthly Expenses    : AED {expenses:.2f}")
    print(f"  Savings Before Tax  : AED {savings:.2f}")
    print(f"  Tax (5%)            : AED {tax:.2f}")
    print(f"  Savings After Tax   : AED {savings_after_tax:.2f}")
    print("=" * 45)