# Automated-Loan-Valuation

### Project Description
This application uses Python 3.7 to automate the valuation of given loans. It will analyze data, complete financial calculations, and save results in a csv file. It was written in Virtual Studio Code and ran/debugged through Terminal using MAC OS Monterey 12.2.1

### Program Contents
1.1 Automate the Calculations

1.2 Analyze Loan Data

1.3 Financial Calculations

1.4 Conditionally Filter Lists of Loans

1.5 Save Results

### Functionality
1.1 The program will automate calculations from this list of loans: [500, 600, 200, 1000, 450]. Specifically, the program will print the number of loans, the total cost of the loans, and the average cost of the loans.

1.2 The program will analyze data from the following loan: {"loan_price": 500, "remaining_months": "repayment_interval": "bullet", "future_value": 1000,}. First, it will extract the values from the keys and create variables for future value and remaining months with values. Then, the program will calculate the fair value of that loan using the present value formula (present value = future value / (1 + annual discount rate/12) ** remaining months). The program will use assigned variables to perform that calculation with the values from the loan and will print the result as the fair value of the loan.

1.3 The program will define a function that can be used to calculate the present value of any given loan which allows the passing of any given data. The function includes parameters for future value, remaining months, and annual discount rate and presents the formula for present value (present value = future value / (1 + annual discount rate/12) ** remaining months) When returned, it will use the given parameters to exectue the calcualtion. For this project, the code will pass the new loan: new_loan = {"loan_price": 800, "remaining_months": 12, "repayment_interval": "bullet", "future_value": 1000,} through the function. Then, it will print the present value of this loan using the information given to the parameters.

1.4 The program is given a list of four loans and will iterate through to select the most inexpensive, given the condition of $500 or less. In doing so, the code will create an empty list, write a conditional statement pulling the key "loan_price" as a value, and appending the new innexpensive loans list with those loans that are less than or equal to $500 in price. The program will then print this new list containaing the inexpensive loans.

1.5 In the beginning of the program, csv was imported from pathlib with Path. This is used to output the list of inexpensive loans that was created, to a new csv file. The program will use a with open function to open a new csv file and will create a 'csvwriter' using the imported library. The code will use the csvwriter to add a header containing labels to better organize the data for the csv file. Then, the program will use a for loop to iterate through the inexpensive loans list and use the csvwriter to write each row of the loan values in the csv file. When run, the csv file will automatically be exported into the user's current directory.

### How to Install and Run the Project
To use this project, you may pull the code from this public repository and run through any CLI using a Python interpreter for versions 3.7+.

### Wrap Up
As my first Python program, I used this project to get familiar with constructing Python code. Specifically, I wanted to practice using functions to perform financial calculations. This code can be translated to answer various problems for organizing and analyzing data. During this project, I learned the importance of DRY code, pseudocode and commenting, and organization. I am excited to use this code as a base to translate to other personal projects or professional problem-solving.

### Contributors
Arlie Jones
arliejones98@gmail.com
Linkedin: https://www.linkedin.com/in/arlie-jones-020092159/
