class Bar:
    def __init__(self, init_sales):
        self.sales = init_sales

    def sell_ticket(self, ticket):
        self.sales += ticket
        return self.sales

    def sell_drink(self, drink):
        self.sales += drink
        return self.sales

    def sell_food(self, food):
        self.sales += food
        return self.sales

    def total_sales(self):
        return self.sales