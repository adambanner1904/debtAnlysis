import numpy as np


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

