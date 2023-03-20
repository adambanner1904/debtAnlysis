import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from simple_debt import Debt
from money import create_dataframe

# y = [17.303, 26.178, 32.995, 39.087, 45.712, 52.002]
# plt.scatter([range(20, 80, 10)], y)
# plt.xlabel("Debt Amount (£1000's)")
# plt.ylabel("Maximum Savings (£1000's)")
# plt.title("How much the maximum savings is per debt amount")
# plt.show()

# Regression analysis to be able to predict from the debt amount at what paying 10%
# repayments will save you money.
# x = np.array([range(20, 80, 10)]).reshape((-1, 1))
# y = np.array(y)
#
# model = LinearRegression().fit(x, y)
# a = model.coef_[0]
# b = model.intercept_
# print(a, b)
#
# x = np.linspace(0, 100).reshape((-1, 1))
# y = model.predict(x)
# plt.plot(x, y)
# plt.show()




# # Working with a debt of 20
# amount = 60
#
# # Going through making minimum repayments
# data_threshold = create_dataframe(amount, 27, 101, 0.09, 27.295)
# data_10 = create_dataframe(amount, 27, 101, 0.1)
# data_20 = create_dataframe(amount, 27, 101, 0.2)
# data_30 = create_dataframe(amount, 27, 101, 0.3)

# with pd.ExcelWriter('amount60.xlsx') as writer:
#     data_threshold.to_excel(writer, sheet_name='Rate=Min')
#     data_10.to_excel(writer, sheet_name='Rate=0.1')
#     data_20.to_excel(writer, sheet_name='Rate=0.2')
#     data_30.to_excel(writer, sheet_name='Rate=0.3')

# plt.plot(range(25, 100), data['Time taken'])
# plt.title("Salary vs Time Taken to Pay Back Loan")
# plt.xlabel("Salary (£1000's)")
# plt.ylabel("Time Taken (Months)")
# plt.show()

# debt.print_time_taken()
# debt.print_payment('debt1')
# debt.print_total_payment('debt1')
# max_amount_paid = data['Total Paid'].max()

data = create_dataframe(30, 20, 101, 0.09, threshold=27.295)
data2 = create_dataframe(50, 20, 101, 0.09, threshold=27.295)
data3 = create_dataframe(70, 20, 101, 0.09, threshold=27.295)

# Plotting the total amount paid against salary when making minimum repayments
# Debt: 30
plt.plot(range(20, 101), data['Total paid'])
# # Debt: 50
plt.plot(range(20, 101), data2['Total paid'])
# # Debt: 70
plt.plot(range(20, 101), data3['Total paid'])
plt.title("Salary vs Total Amount Paid From Minimum Repayments")
plt.xlabel("Salary (£1000's)")
plt.ylabel("Total Amount Paid (£1000's)")
# plt.vlines(27.295, 0, 110, linestyles='--', colors='red')
# plt.vlines(67.5, 0, 110, linestyles='--', colors='red')
plt.legend(['Debt: £30,000', 'Debt: £50,000', 'Debt: £70,000'])
# plt.text(18, 80, 'Stage 1').set_rotation(45)
# plt.text(40, 80, 'Stage 2')
# plt.text(85, 40, 'Stage 3')
plt.show()












# debt2.print_time_taken()
# print(f'Amount saved: {amount_saved(debt, debt2)}')
# debt2.print_payment('debt2')
# debt2.print_total_payment('debt2')
# debt = Debt(30, 40, 0.1, 0.06)
# debt2 = Debt(30, 50, 0.1, 0.06)
# debt.wipe_debt()
# debt2.wipe_debt()
#
# debt.plot_payment_history("red")
# debt2.plot_payment_history("green")
# debt2.plot_debt_history("blue")
# plt.hlines(30, 0, len(debt.payment_history))
# plt.hlines(debt.total_payment, 0, len(debt.payment_history), linestyles='--', label='Total amount paid')
# plt.hlines(debt2.total_payment, 0, len(debt2.payment_history), linestyles='--', label='Total amount paid')
# plt.ylabel('Pounds (Thousands)')
# plt.xlabel('Time (Months)')
# plt.legend(['Payment History with threshold payments', 'Payment History without threshold payments',
#             'Amount of original debt'])
# plt.show()
