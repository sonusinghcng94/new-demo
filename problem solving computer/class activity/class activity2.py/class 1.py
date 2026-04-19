# ============================================================
#          PRACTICE PROBLEM 1 – Calculate Percentage
# ============================================================

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  [Error] Value cannot be negative.")
            else:
                return value
        except ValueError:
            print("  [Error] Please enter a valid number.")

print("=" * 45)
print("        PERCENTAGE CALCULATOR")
print("=" * 45)

marks_obtained = get_positive_float("  Marks Obtained : ")
total_marks    = get_positive_float("  Total Marks    : ")

if total_marks == 0:
    print("\n  [Error] Total marks cannot be zero.")
else:
    percentage = (marks_obtained / total_marks) * 100

    print("\n" + "-" * 45)
    print(f"  Marks Obtained : {marks_obtained}")
    print(f"  Total Marks    : {total_marks}")
    print(f"  Percentage     : {percentage:.2f}%")

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"  Grade          : {grade}")
    print("=" * 45)