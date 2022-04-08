class Room:
    def __init__(self, init_name, init_guests, init_songs):

        self.name = init_name
        self.guests = init_guests
        self.songs = init_songs
    
    def total_guests_in_room(self):
        return len(self.guests)

    def check_in_guest_to_room(self, guest):
        self.guests.append(guest)

    def check_out_guests_from_room(self, guest):
        self.guests.remove(guest)
    
    def total_songs_in_room(self):
        return len(self.songs)
    
    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)