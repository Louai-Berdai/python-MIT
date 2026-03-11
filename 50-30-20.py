Salary = int(input("Enter your salary:  ").strip())
needs = float(Salary) / 2
savings = float(Salary) / 5
wants = float(Salary) - (needs + savings)
print(f"Based on your salary of {Salary}, you should have {savings} in savings, {wants} for wants, and {needs} for needs.")