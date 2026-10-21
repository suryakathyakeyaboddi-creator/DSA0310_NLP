
import re

# Student registration details
student = {
    "Register Number": "192425028",
    "Institutional Email": "192425028@college.edu.in",
    "Course Code": "CSE101",
    "Semester": "Semester 3",
    "Mobile Number": "9876543210"
}

# Regular expression patterns
patterns = {
    "Register Number": r"^\d{9}$",
    "Institutional Email": r"^[A-Za-z0-9._%+-]+@college\.edu\.in$",
    "Course Code": r"^[A-Z]{3}\d{3}$",
    "Semester": r"^Semester\s[1-8]$",
    "Mobile Number": r"^[6-9]\d{9}$"
}

# Validation function
def validate_field(field, value, pattern):
    if re.fullmatch(pattern, value, re.IGNORECASE):
        print(f"{field}: {value} -> Valid")
        return True
    else:
        print(f"{field}: {value} -> Invalid")
        return False

# Validate all student details
print("=" * 55)
print("     UNIVERSITY REGISTRATION VALIDATION")
print("=" * 55)

validation_results = {}

for field, value in student.items():
    validation_results[field] = validate_field(
        field, value, patterns[field]
    )

# Generate final registration report
print("\n" + "=" * 55)
print("        FINAL REGISTRATION STATUS REPORT")
print("=" * 55)

for field, is_valid in validation_results.items():
    print(f"{field}: {'PASS' if is_valid else 'FAIL'}")

if all(validation_results.values()):
    print("\nRegistration Status: SUCCESSFUL")
    print("All student details are valid.")
else:
    print("\nRegistration Status: FAILED")
    print("Please correct the invalid student details.")

print("=" * 55)
