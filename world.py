import npc
import items


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self, player):
        raise NotImplementedError("Create a subclass please!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def __init__(self, x, y):

        self.game_start_text = """
        Hello, I'm Ollie the Penguin!! 
        
        I hope you can help me, I've been left to clean up after a big picnic we all had
        and I'm sure some of my friends have run off with the wrong items!! Silly Billies!
        
        Let's get them back to the right people!
        
        But first, we'll need to find them!! 
        
        """
        self.game_playing_text = """
        
        A lovely patch of green grass!
        
        """

        super().__init__(x, y)

    def intro_text(self, player):
        if not player.game_started:
            text = self.game_start_text
            StartTile.modify_player(self, player)
        else:
            text = self.game_playing_text

        return text

    def modify_player(self, player):
        player.game_started = True


class VictoryTile(MapTile):
    def intro_text(self, player):
        # if any(isinstance(x, items.SnortScarf) for x in player.inventory) and \
        #         not any(isinstance(x, items.HootsScrolls) for x in player.inventory) and \
        #         not any(isinstance(x, items.TinyTickleSwordHat) for x in player.inventory) and \
        #         not any(isinstance(x, items.JeffBlankey) for x in player.inventory) and \
        #         not any(isinstance(x, items.WaddlesTapShoes) for x in player.inventory):
        if not any(isinstance(x, items.QuestItem) for x in player.inventory):
            print(""""
            
            Ollie: Ah, excellent! I've made it home and completed all my deliveries!
            
            Time for the bedtime song I think!
            
            Bedtime song, this is the bedtime song! 
            Time to get cosy and dim the lights!
            Bed time song, this is the bedtime song! 
            Give each others kisses (mwah)
            And then say "Night Night!"
            
            
            Congratulations, you've helped Ollie help his friends and got him home safely!
            
            Good job!!
            
            """)
            # self.modify_player(player)
            # return
        else:
            print("""
            
            I should probably get all my friends' things back to them!
            
            """)

    # def modify_player(self, player):
    #     player.victory = True


class CharacterTile(MapTile):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y)

    def intro_text(self, player):
        raise NotImplementedError("Create a subclass please!")

    def modify_player(self, player):
        pass

    def check_if_trade(self, player):
        while True:
            print("Would you like to T(ake), (G)ive, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['T', 't']:
                print("Here's whats available to take: ")
                self.trade(buyer=player, seller=self.character)
            elif user_input in ['G', 'g']:
                print("Here's whats available to give: ")
                self.trade(buyer=self.character, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}: {} - {}".format(i, item.name, item.description))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        print("Swap Complete")


class JeffTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.Jeff()
        super().__init__(x, y)

    def intro_text(self, player):
        if any(isinstance(x, items.JeffBlankey) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class TinyTicklesTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.TinyTickles()
        super().__init__(x, y)

    def intro_text(self, player):
        if any(isinstance(x, items.TinyTickleSwordHat) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class SnortTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.Snort()
        super().__init__(x, y)

    def intro_text(self, player):
        if any(isinstance(x, items.SnortScarf) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class WaddlesTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.Waddles()
        super().__init__(x, y)

    def intro_text(self, player):
        if any(isinstance(x, items.WaddlesTapShoes) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class HootsTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.Hoots()
        super().__init__(x, y)

    def intro_text(self, player):
        if any(isinstance(x, items.HootsScrolls) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class LawrenceTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.Lawrence()
        super().__init__(x, y)

    def intro_text(self, player):
        if not any(isinstance(x, items.WaddlesTapShoes) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class BabyBunnyTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.BabyBunny()
        super().__init__(x, y)

    def intro_text(self, player):
        if not any(isinstance(x, items.JeffBlankey) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class BertieTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.Bertie()
        super().__init__(x, y)

    def intro_text(self, player):
        if not any(isinstance(x, items.TinyTickleSwordHat) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class OsianTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.Osian()
        super().__init__(x, y)

    def intro_text(self, player):
        if not any(isinstance(x, items.HootsScrolls) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class DizzyTile(CharacterTile):
    def __init__(self, x, y):
        self.character = npc.Dizzy()
        super().__init__(x, y)

    def intro_text(self, player):
        if not any(isinstance(x, items.SnortScarf) for x in self.character.inventory):
            print(self.character.happy_text)
        else:
            return self.character.text


class SignPostNorth(MapTile):
    def intro_text(self, player):
        return """
        
        There's some noise coming from the North!
        
        """


class SignPostNorthEast(MapTile):
    def intro_text(self, player):
        return """
        
        There's some noise coming from the North East!
        
        """


class SignPostEast(MapTile):
    def intro_text(self, player):
        return """
        
        There's some noise coming from the East!
        
        """


class SignPostSouthEast(MapTile):
    def intro_text(self, player):
        return """
        
        There's some noise coming from the South East!
        
        """


class SignPostSouth(MapTile):
    def intro_text(self, player):
        return """
        
        There's some noise coming from the South!
        
        """


class SignPostSouthWest(MapTile):
    def intro_text(self, player):
        return """
        
        There's some noise coming from the South West!
        
        """


class SignPostWest(MapTile):
    def intro_text(self, player):
        return """
        
        There's some noise coming from the West!
        
        """


class SignPostNorthWest(MapTile):
    def intro_text(self, player):
        return """
        
        There's some noise coming from the North West!
        
        """


class SignPostOllieHouse(MapTile):
    def intro_text(self, player):
        return """
        
        Ollie: I'm sure my house is nearby!!
        
        Ollie was out playing with Jeff, Snort, Dizzy, Bertie, Professor Hoots, Baby Bunny, Lawrence, Osian and Waddles! 
        
        Have you found them all yet?
        
        """


class GreenGrass(MapTile):
    def intro_text(self, player):
        return """
        
        What lovely green grass
        
        """


tile_type_dict = {"VT": VictoryTile,
                  "JF": JeffTile,
                  "SN": SnortTile,
                  "DZ": DizzyTile,
                  "BT": BertieTile,
                  "PH": HootsTile,
                  "TT": TinyTicklesTile,
                  "ST": StartTile,
                  "BB": BabyBunnyTile,
                  "LW": LawrenceTile,
                  "OS": OsianTile,
                  "WD": WaddlesTile,
                  "SOH": SignPostOllieHouse,
                  "SPN": SignPostNorth,
                  "SNE": SignPostNorthEast,
                  "SE": SignPostEast,
                  "SSE": SignPostSouthEast,
                  "SS": SignPostSouth,
                  "SSW": SignPostSouthWest,
                  "SW": SignPostWest,
                  "SNW": SignPostNorthWest,
                  "  ": GreenGrass}


world_dsl = """
|  |JF|  |  |  |  |SOH|SOH|SOH|
|SSE|  |SNW|SE|  |SN|SOH|VT|SOH|
|  |DZ|  |  |  |  |SOH|SOH|SOH|
|SS|SPN|  |BT|  |SPN|  |  |SSW|
|PH|  |SNE|  |  |SE|  |TT|SW|
|  |SNW|  |ST|  |BB|  |  |SNW|
|SSW|SS|SSE|  |SNE|  |  |  |  |
|  |LW|  |OS|  |SS|  |  |  |
|SNE|  |SN|  |WD|  |  |  |  |
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


world_map = []

start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
