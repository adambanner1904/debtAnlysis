# Creating a debt class
class Debt:

    def __init__(self, amount, salary, payback_rate, interest_rate):

        self.amount = amount
        self.ir = interest_rate
        self.pbr = payback_rate

        # Calculating income after tax
        self.salary = salary

        if self.salary <= 12.570:
            self.income = self.salary
        elif 12.570 < self.salary <= 50.270:
            pa = 12.570
            br = self.salary - pa
            self.income = pa + br * 0.8
        elif 50.270 < self.salary <= 150.0000:
            pa = 12.570
            br = 50.270 - 12.570
            hr = self.salary - br - pa
            self.income = pa + br * 0.8 + hr * 0.6
        elif 150.000 < self.salary:
            pa = 12.570
            br = 50.270 - 12.570
            hr = 150.000
            ar = self.salary - hr - br - pa
            self.income = pa + br * 0.8 + hr * 0.6 + ar * 0.55

        # Calculating monthly payments and tracking payments
        self.payment = self.income * self.pbr/12
        self.total_payment = 0

        # Used to track the interest
        self.interest = 0

        # Used to keep track of how long it takes to pay a debt
        self.years = 0
        self.months = 0

    def accumulate_interest(self):
        """Interest is yearly"""

        self.amount += self.amount * self.ir
        self.interest += self.amount * self.ir

    def make_payment(self):
        """Making a monthly payment."""
        # If the amount is positive, if there is still a debt, then continue to making a payment
        if self.check_amount():
            self.amount -= self.payment
        else:
            print("There is no more debt")

    def check_amount(self):
        """Checks to see if the amount of the debt is positive and if the next payment
        will make the debt negative. Returns true (1) if there is still an amount and
        false (0) if the debt is done."""
        if self.amount <= 0 or self.amount - self.income * self.pbr/12 < 0:
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


debt = Debt(50, 25, 0.09, 0.06)

print(f'Starting debt is: {debt.amount}')
print(f'Salary is {debt.salary}, Income is {debt.income}')
while debt.check_amount():
    debt.pass_year()
    if debt.years == 31:
        break
    print(f'Year {debt.years}: {debt.amount}')
print(f'It took {debt.years} years and {debt.months} months')
print(f'Total interest: {debt.interest}')

