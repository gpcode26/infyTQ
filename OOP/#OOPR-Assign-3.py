#OOPR-Assign-3

class Customer:

    def __init__(self):
        self.customer_name = None
        self.bill_amount = None

    def purchases(self):
        self.bill_amount = self.bill_amount - self.bill_amount * (5 / 100)

    def pays_bill(self, amount):
        self.bill_amount += amount
        self.purchases()
        print(self.customer_name, "pays bill amount of Rs.", self.bill_amount)
