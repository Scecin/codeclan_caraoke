class Guest:
    def __init__(self,init_name, init_cash):
        self.name = init_name
        self.cash = init_cash
    
    def sufficient_founds(self, room):
        return self.cash >= room.price

    def pay_entry_fee(self, room):
        if self.sufficient_founds(room):
           self.cash -= room.price
           return self.cash
