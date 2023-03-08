

# Creating a debt class
class Debt:

    def __init__(self, amount, salary, payback_rate, interest_rate, pay_interval='m', interest_interval = 'y'):

        self.amount = amount
        self.ir = interest_rate
        self.pay_interval = pay_interval
        self.salary = salary
        self.pbr = payback_rate
        self.interest_interval = interest_interval

    def accumulate_interest(self):

        self.amount += self.amount * self.ir

    def make_payment(self):

        # If the amount is positive, if there is still a debt, then continue to making a payment
        if self.amount > 0 or not self.amount - self.salary * self.pbr:
            self.amount -= self.salary * self.pbr
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
        """There are three options for both the interest accumulation interval and
        the payment transaction interval. The outer if statements are where the interest interval is daily
        monthly or yearly as these are the most common. The inner if statements all cycle through where the
        payments are made daily, weekly or monthly working on the assumption that debts are not really
        paid yearly. The default settings for the Debt class are making payments monthly and interest yearly."""
        self.days = 0

        # If the interest is daily
        if self.interest_interval.lower() == 'd':

            # If the payments are made daily
            if self.pay_interval.lower() == 'd':

                for d in range(365):

                    self.accumulate_interest()
                    self.make_payment()


            # If payments are made weekly
            if self.pay_interval.lower() == 'w':

                # Make payment once a week
                for w in range(52):
                    self.make_payment()

                    # Accumulate interest every day of every week
                    for d in range(7):
                        self.accumulate_interest()

            # If payments are made monthly
            if self.pay_interval.lower() == 'm':

                # Make payment once a month
                for m in range(12):
                    self.make_payment()

                    # Accumulate interest every day every month
                    for d in range(30):
                        self.accumulate_interest()
        ########################
        # If the interest is monthly
        if self.interest_interval.lower() == 'm':

            # If payments are made daily
            if self.pay_interval.lower() == 'd':

                # Accumulate interest once a month
                for m in range(12):
                    self.accumulate_interest()

                    # Make payment every day every month
                    for d in range(30):
                        self.make_payment()

            # If payments are made weekly
            if self.pay_interval.lower() == 'w':

                # Accumulate interest once a month
                for m in range(12):
                    self.accumulate_interest()

                    # Make payment every week of every month
                    for w in range(4):
                        self.make_payment()


            # If payments are made monthly
            if self.pay_interval.lower() == 'm':

                # Make payment once a month
                for m in range(12):
                    self.make_payment()
                    self.accumulate_interest()

        ########################
        # If the interest is yearly
        if self.interest_interval.lower() == 'y':

            # If payments are made daily
            if self.pay_interval.lower() == 'd':

                # Accumulate interest once a year
                self.accumulate_interest()

                # Make payment every day of the year
                for d in range(365):
                    self.make_payment()

            # If payments are made weekly
            if self.pay_interval.lower() == 'w':

                # Accumulate interest once a year
                self.accumulate_interest()

                # Make payment every week of the year
                for w in range(52):
                    self.make_payment()

            # If payments are made monthly
            if self.pay_interval.lower() == 'm':

                # Accumulate interest once a year
                self.accumulate_interest()

                # Make payment every month of the year
                for m in range(12):

                    if self.check_amount():
                        self.make_payment()
                    else:
                        break
                    self.days += 30



debt = Debt(40, 40, 0.1, 0.06)

print(debt.amount)
debt.pass_year()
print(debt.days)

print(debt.amount)

