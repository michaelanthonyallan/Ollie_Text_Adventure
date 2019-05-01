import world


class Player:
    def __init__(self):
        self.inventory = []
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.victory_points = 0
        self.victory = False
        self.game_started = False

    def print_inventory(self):
        for item in self.inventory:
            print("""
            > """ + str(item))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def game_started(self):
        return self.game_started

    def victory_count(self):
        return self.victory_points

    def sleep(self):
        return "Sleepy times!"
