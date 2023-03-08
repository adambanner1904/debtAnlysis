# Creating a debt class
class Debt:

    def __init__(self, amount, salary, payback_rate, interest_rate):

        self.amount = amount
        self.ir = interest_rate
        self.salary = salary
        self.pbr = payback_rate

        # Used to keep track of how long it takes to pay a debt
        self.years = 0
        self.months = 0


    def accumulate_interest(self):

        self.amount += self.amount * self.ir

    def make_payment(self):
        """Making a monthly payment. """
        # If the amount is positive, if there is still a debt, then continue to making a payment
        if self.amount > 0 or not self.amount - self.salary * self.pbr/12:
            self.amount -= self.salary * self.pbr/12
        else:
            print("There is no more debt")

    def check_amount(self):
        """Checks to see if the amount of the debt is positive and if the next payment
        will make the debt negative. Returns true (1) if there is still an amount and
        false (0) if the debt is done."""
        if self.amount <= 0 or self.amount - self.salary * self.pbr < 0:
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
                break

        # Accumulate interest once a year
        self.accumulate_interest()

    def pass_month(self):
        pass
        # Make payment



debt = Debt(40, 40, 0.1, 0.06)

print(debt.amount)
debt.pass_year()
print(debt.months)

print(debt.amount)
