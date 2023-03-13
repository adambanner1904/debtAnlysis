import matplotlib.pyplot as plt
import pandas as pd
from simple_debt import Debt
from money import amount_saved

amount = 50
data = pd.DataFrame(columns=['Total Paid'])
for salary in range(25, 100):
    debt = Debt(amount, salary, 0.09, 0.06, threshold=27.995)
    debt.wipe_debt()
    df = pd.DataFrame()
    data.loc[salary] = debt.total_payment

# debt.print_time_taken()
# debt.print_payment('debt1')
# debt.print_total_payment('debt1')
data.plot(y='Total Paid')














# debt2.print_time_taken()
# print(f'Amount saved: {amount_saved(debt, debt2)}')
# debt2.print_payment('debt2')
# debt2.print_total_payment('debt2')


# debt.plot_payment_history("red")
# debt2.plot_payment_history("green")
# debt2.plot_debt_history("blue")
# plt.hlines(amount, 0, len(debt.payment_history))
# plt.hlines(debt.total_payment, 0, len(debt.payment_history), linestyles='--', label='Total amount paid')
# plt.hlines(debt2.total_payment, 0, len(debt2.payment_history), linestyles='--', label='Total amount paid')
# plt.ylabel('Pounds (Thousands)')
# plt.xlabel('Time (Months)')
# plt.legend(['Payment History with threshold payments', 'Payment History without threshold payments', 'Amount of original debt'])
# plt.show()