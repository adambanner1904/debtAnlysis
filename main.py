from simple_debt import Debt
import matplotlib.pyplot as plt


debt = Debt(50, 50, 0.09, 0.06, threshold=27.995)

print(f'Starting debt is: {debt.amount}')
print(f'Starting salary is: {debt.salary}')
print(f'Payments are {debt.payment * 1000}')
# print(f'Salary is {debt.salary}, Income is {debt.income}')
while debt.check_amount():
    debt.pass_year()
    if debt.years == 31:
        break
#     print(f'Year {debt.years}: {debt.amount}')
print(f'It took {debt.years} years and {debt.months} months')
print(f'Total interest: {debt.total_interest}')
print(f'Total paid: {debt.total_payment}')
# print(debt.payment_history)