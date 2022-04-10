class Bar:
    def __init__(self, init_sales):
        self.sales = init_sales

    def increase_entry_fee(self, entry_fee_price):
        self.sales += entry_fee_price

    def increase_drink_price(self, drink_price):
        self.sales += drink_price

    def increase_food_price(self, food_price):
        self.sales += food_price

    def total_sales(self):
        return self.sales