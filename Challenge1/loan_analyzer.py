import csv
from pathlib import Path

print("-----------------------------------------------------------")
print("----AUTOMATING CALCULATIONS----")

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

loans_in_list = len(loan_costs) #Using the len function to calculate the number of loans in the loan_costs list and assigned it to the variable - loans_in_list
print("The total number of loans in this list are: ",loans_in_list) #Print the result of the len function above with a string description

total_cost_of_loans = sum(loan_costs) #Using the sum function to calculate the sum of loans in the loan_costs list and assigned it to the variable - total_cost_of_loans
print("The total value of all loans in this list is: $",total_cost_of_loans) #Print the result of the sum function above with a string description

average_loan_amt = (total_cost_of_loans/loans_in_list) #Using basic logic of average function (sum/n). Both the sum and n are already assigned to variables above, so write the function as total_cost_of_loans/loans_in_list to return the average and assign it to the variable - average_loan_amount
print("The average loan amount is: $",average_loan_amt) #Print the result of the calculation above with a string description

print("-----------------------------------------------------------")
print("----ANALYZE LOAN DATA----")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value") #Use get() on the loan dictionary to extract the future value key from the string "future_value"
remaining_months = loan.get("remaining_months") #Use get() on the loan dictionary to extract the remaining months key from the string "remaining_months"
print("Future Value: ",future_value) #Print the future value with string description
print("Remaining Months: ",remaining_months) #Print the remaining months with string description

# Use a minimum required return of 20% as the discount rate.

fair_value = future_value / (1+.20/12) ** remaining_months #Use present value formula to calcuate the fair value of the loan using the assigned variables, and .2 as the dscount rate
print("The fair value of the loan is:",fair_value) #Print the result of the above calculation with a string description 

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?

# If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
# Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
if fair_value >= loan.get("loan_price"): #If statement to show the if present value is greater than or equal to the loan price
    print("The loan is worth at least the cost to buy it") #If true, print the loan is worth to buy at price
else: #If the present value is less than the loan price
    print("The loan is too expensive and not worth the price") #Print the loan is too expensive

print("-----------------------------------------------------------")
print("----FINANCIAL CALCULATIONS----")

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

def calculate_present_value(future_value, remaining_months, annual_discount_rate): # Define New function to calculate present value using parameters future value, remaining months, and annual discount rate
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months #Set present value caluclation for function to perform 
    return present_value #Return the above value to be able to reference in the rest of the code

present_value_of_new_loan = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], 0.2) #To calculate present value of new loan from dictionary above, call the function -calculate_present_value with the parameters future value(extracted from dict using[]), remaining months(extracted from dict using[]), and an input of 0.2 for the discount rate

print(f"The present value of the new loan is: {present_value_of_new_loan}") #Print the result of above calculation with an f string definition


print("-----------------------------------------------------------")
print("----FILTERING LOAN LIST----")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

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

inexpensive_loans = [] # Create an empty list called inexpensive_loans

for price in loans: #Loop through all the loans in above dictionary
    loan_price = price["loan_price"] #Assign the price value to variable loan_price retrived from the keystring in above dictionary
    if loan_price <= 500: #If the loan price is is 500 or less...
        inexpensive_loans.append(price) #Append that whole loan to the inexensive loans list, meaning to add it to the empty list created earlier
        

print("The inexpensive loans list is:,", 
inexpensive_loans) #Print the inexpensive loans list which will include loans that are $500 or less

print("-----------------------------------------------------------")
print("----INEXPENSIVE LOANS LIST WILL BE EXPORTED IN CSV FILE----")

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects"""

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"] #Set the output header for the csv file

csvpath = Path("inexpensive_loans.csv") #Set the path for the csv file by assigning it to the variable csvpath and using the imported Path from pathlib

with open(csvpath, "w") as csvfile: #Use with open statement to open csv file as a write file
    csvwriter = csv.writer(csvfile, delimiter=",") #Create the writer

    csvwriter.writerow(header) #Use the csvwriter to write the header row to better organize data in csv file

    for loan in inexpensive_loans: #Use a for loop to iterate through the inexpensive loans list
        csvwriter.writerow(loan.values()) #Use the csvwriter to write each row of the loan values in the csv file