class Guest:
    def __init__(self,init_name, init_cash, init_favourite_song):
        self.name = init_name
        self.cash = init_cash
        self.favourite_song = init_favourite_song
    
    def sufficient_founds(self, room):
        return self.cash >= room.price

    def spend_cash(self, amount):
        self.cash -= amount

