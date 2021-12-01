import csv
from pathlib import Path

# @TODO: Part 1: Automate the Calculations.

loan_costs = [500, 600, 200, 1000, 450]

# Calculate and print the total loan number
total_loan_number = len(loan_costs)
print(f"The total number of loans is: {total_loan_number}.")

# Calculate and print the total loan amount
total_loan_amount = sum(loan_costs)
print(f"The total loan amount is: ${total_loan_amount:.2f}.")

# Calculate and print the average loan price
average_loan_price = total_loan_amount / total_loan_number
print(f"Therefore, the average loan price is: ${average_loan_price:.2f}.")


# @TODO: Part 2: Analyze Loan Data.


loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extract future value and remaining months from a dictionary using the get() method
future_value = loan.get("future_value")
print(f"The expected future value of the loan is: ${future_value:.2f}.")

remaining_months = loan.get("remaining_months")
print(f"And, the remaining months on the loan is: {remaining_months}")


# Calculated present value using a non-defined formula and assigned it to a variable
present_value = future_value / (1 + 0.2/12)**remaining_months


# Wrote conditional statements to determine and print the value of a loan and whether to buy or not
if present_value >= loan["loan_price"]:
    print(f"For ${loan.get('loan_price')}, the loan is worth at least the cost to buy for an estimated fair value of: "
          f"${present_value:.2f}.")
else:
    print(f"At a fair value of ${present_value:.2f}, the loan is too expensive at "
          f"${loan.get('loan_price')} and not worth the cost.")


# @TODO: Part 3: Perform Financial Calculations.


# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Defined a new function to calculate a present value using previous formula and given parameters
# "present_value" is not returned as it would be shadowing a globally scoped variable and I don't want mild-warnings


def calculate_present_value(a_future_value, a_annual_discount_rate, a_remaining_months):
    a_present_value = a_future_value / (1 + a_annual_discount_rate/12)**a_remaining_months
    return a_present_value


# Calculated the present value for a specific loan using the calculate_present_value function defined above
annual_discount_rate = 0.2

present_value = calculate_present_value(
    new_loan['future_value'],
    annual_discount_rate,
    new_loan['remaining_months']
)
print(f"The present value of the loan is: ${present_value:.2f}")


# @TODO: Part 4: Conditionally filter lists of loans.


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Extracted loans less than or equal to $500 and appended them to an empty list titled inexpensive_loans
inexpensive_loans = []
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)
print(f"Your list of loans with a price less than or equal to $500 is {inexpensive_loans}.")


# @TODO: Part 5: Save the results.


print("Writing the data to a CSV file...")

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Wrote header and inexpensive_loans to a CSV file
with open(output_path, 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(header)
    for loan in inexpensive_loans:
        csv_writer.writerow(loan.values())
