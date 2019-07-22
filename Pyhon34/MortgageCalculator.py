numOfMonths = int(input('Enter number of periodic payments: ')) * 12
interestRate = (int(input('Enter periodic interest rate: ')) / 100) / 12
LoanAmount = float(input('Enter amount of loan: '))

# Number of Periodic Payments (n) = Payments per year times number of years
# Periodic Interest Rate (i) = Annual rate divided by number of payments per
# Discount Factor (D) = {[(1 + i) ^n] - 1} / [i(1 + i)^n] (formula!)

DiscountFactor = ((((1 + interestRate)**numOfMonths) - 1) / (interestRate * ((1 + interestRate)**numOfMonths)))

# Loan payment = Loan amount / Discount factor
LoanPayment = LoanAmount / DiscountFactor
print('Your monthly loan payment is ${0:.2f}'.format(LoanPayment))
print('Your total loan payment is ${0:.2f}'.format(LoanPayment * numOfMonths))