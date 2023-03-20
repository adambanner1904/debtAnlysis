import numpy as np
from simple_debt import Debt
import pandas as pd


def tax(salary):
    if salary <= 12.570:
        income = salary
    elif 12.570 < salary <= 50.270:
        pa = 12.570
        br = salary - pa
        income = pa + br * 0.8
    elif 50.270 < salary <= 150.0000:
        pa = 12.570
        br = 50.270 - 12.570
        hr = salary - br - pa
        income = pa + br * 0.8 + hr * 0.6
    elif 150.000 < salary:
        pa = 12.570
        br = 50.270 - 12.570
        hr = 150.000
        ar = salary - hr - br - pa
        income = pa + br * 0.8 + hr * 0.6 + ar * 0.55

    return income


# Takes in two debts and subtracts one total payment from another to work out
# the difference which is the amount saved
def amount_saved(debt1, debt2):
    amount_saved = np.abs(debt1.total_payment - debt2.total_payment)
    return amount_saved


def create_dataframe(debt_amount, test_start_salary, test_finish_salary, pb_rate, threshold=0):
    """Creates and returns a pandas dataframe, that has index column, the salary, total paid
    for that salary making the payments that you define by percentage of salary and if it has
    a threshold or not."""

    df = pd.DataFrame(columns=['Salary', 'Total paid', 'Years', 'Months'])
    for idx, salary in enumerate(range(test_start_salary, test_finish_salary)):
        debt = Debt(debt_amount, salary, pb_rate, 0.06, threshold=threshold)
        debt.wipe_debt()
        df.loc[idx] = [salary, debt.total_payment, debt.years, debt.months]

    return df
