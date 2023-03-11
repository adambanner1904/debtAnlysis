from simple_debt import Debt
import matplotlib.pyplot as plt
amount = 50

debt = Debt(amount, 50, 0.09, 0.06, threshold=27.995)
debt_without_threshold = Debt(amount, 50, 0.2, 0.06)


while debt.check_amount():
    debt.pass_year()
    if debt.years == 31:
        break

while debt_without_threshold.check_amount():
    debt_without_threshold.pass_year()
    if debt_without_threshold.years == 31:
        break


debt.plot_payment_history("red")
debt_without_threshold.plot_payment_history("green")
debt_without_threshold.plot_debt_history("blue")
plt.hlines(amount, 0, len(debt.payment_history))
plt.ylabel('Pounds (Thousands)')
plt.xlabel('Time (Months)')
plt.legend(['Payment History with threshold payments', 'Payment History without threshold payments', 'Amount of original debt'])
plt.show()