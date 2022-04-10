from multiprocessing import cpu_count
from unicodedata import name

from src.guest import Guest
from src.bar import Bar


class Room:
    def __init__(self, init_name, init_guests, init_songs, init_price, init_bar):

        self.name = init_name
        self.guests = init_guests
        self.songs = init_songs
        self.price = init_price
        self.bar = init_bar
    
    def total_guests_in_room(self):
        return len(self.guests)

    def check_in_guest_to_room(self, guest, room):
        capacity = self.total_guests_in_room()
        has_money = guest.sufficient_founds(room)
        if capacity < 4 and has_money == True:
            self.guests.append(guest)
            capacity += 1
        elif has_money == False:
            return "Funds are insufficient. Please try again later."
        else:
            return "Sorry, the room is full. Please try again later."

    def check_out_guests_from_room(self, guest):
        self.guests.remove(guest)
    
    def total_songs_in_room(self):
        return len(self.songs)
    
    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)

    def favourite_song_in_room(self, favourite_song):
        for song in self.songs:
            if song.name == favourite_song:
                return "Whoo!"
    
    def sell_entry_fee (self, guest, bar, ticket_price):
        guest.spend_cash(ticket_price)
        bar.increase_entry_fee(ticket_price)
    
        