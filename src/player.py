# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, player_room, inventory=[]):
        self.name = name
        self.player_room = player_room
        self.inventory = inventory

    def move(self, direction):
        next_move = getattr(self.player_room, f"{direction}_to")
        if next_move is not None:
            self.player_room = next_move
            print(self.player_room)

    def get_item(self):
        pass
    def drop_item(self):
        pass

    def __str__(self):
        return (f"{self.player_room}")