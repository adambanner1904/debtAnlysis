from simple_debt import Debt
from money import amount_saved
import matplotlib.pyplot as plt
amount = 50

debt = Debt(amount, 60, 0.09, 0.06, threshold=27.995)
debt2 = Debt(amount, 60, 0.3, 0.06)


debt.wipe_debt()

debt2.wipe_debt()


debt.print_time_taken()
debt2.print_time_taken()
print(f'Amount saved: {amount_saved(debt, debt2)}')
print(f'Payments for plan 1: {debt.payment}, Payment for plan 2: {debt2.payment}')


# debt.plot_payment_history("red")
# debt_without_threshold.plot_payment_history("green")
# debt_without_threshold.plot_debt_history("blue")
# plt.hlines(amount, 0, len(debt.payment_history))
# plt.hlines(debt.total_payment, 0, len(debt.payment_history), linestyles='--', label='Total amount paid')
# plt.ylabel('Pounds (Thousands)')
# plt.xlabel('Time (Months)')
# plt.legend(['Payment History with threshold payments', 'Payment History without threshold payments', 'Amount of original debt'])
# plt.show()