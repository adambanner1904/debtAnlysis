# Creating a debt class
import matplotlib.pyplot as plt


class Debt:

    def __init__(self, amount, salary, payback_rate, interest_rate, threshold=0):

        self.amount = amount
        self.ir = interest_rate
        self.pbr = payback_rate
        self.salary = salary

        # Calculating monthly payments and tracking payments
        if threshold:
            if self.salary < threshold:
                self.payment = 0
            else:
                self.payment = (self.salary - threshold) * self.pbr / 12
        else:
            self.payment = self.salary * self.pbr/12

        self.total_payment = 0
        self.payment_history = []

        # Used to track the interest
        self.total_interest = 0
        self.interest_history = []

        # Used to keep track of how long it takes to pay a debt
        self.years = 0
        self.months = 0

    def accumulate_interest(self):
        """Interest is yearly"""

        self.amount += self.amount * self.ir
        self.total_interest += self.amount * self.ir
        self.interest_history.append(self.total_interest)

    def make_payment(self):
        """Making a monthly payment."""
        # If the amount is positive, if there is still a debt, then continue to making a payment
        self.amount -= self.payment
        self.total_payment += self.payment
        self.payment_history.append(self.total_payment)

    def check_amount(self):
        """Checks to see if the amount of the debt is positive and if the next payment
        will make the debt negative. Returns true (1) if there is still an amount and
        false (0) if the debt is done."""
        if self.amount <= 0 or self.amount - self.payment < 0:
            return 0
        else:
            return 1

    def pass_year(self):
        """The interest is added at the end of the year"""

        # Make payment every month of the year
        for m in range(12):

            if self.check_amount():
                self.make_payment()
                self.months += 1
            else:
                return
        self.years += 1
        self.months = 0
        # Accumulate interest once a year
        self.accumulate_interest()

    def pass_month(self):
        pass
        # Make payment

    def plot_payment_history(self, color='blue'):
        plt.plot(range(len(self.payment_history)), self.payment_history, c=color)




