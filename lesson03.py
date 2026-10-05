def calculate_risk(likelihood, impact):
    return likelihood * impact


likelihood = int(input("Enter likelihood (1-5): "))
impact = int(input("Enter impact (1-5): "))

if not (1 <= likelihood <= 5 and 1 <= impact <= 5):
    print("Both scores must be between 1 and 5.")
else:
    risk = calculate_risk(likelihood, impact)

    print(f"Risk score: {risk}/25")
