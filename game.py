from collections import OrderedDict
import world
from player import Player


def play():
    print("Ollie's Adventure!")
    world.parse_world_dsl()
    player = Player()
    while not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text(player))
        room.modify_player(player)
        choose_action(room, player)


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("You can't do that, try something else!")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory")
    if isinstance(room, world.VictoryTile):
        action_adder(actions, 's', player.sleep, "Sleep")
    else:
        pass
    if isinstance(room, world.CharacterTile):
        action_adder(actions, 't', player.trade, "Trade")
    if world.tile_at(room.x, room.y - 1):
        action_adder(actions, 'n', player.move_north, "Go North")
    if world.tile_at(room.x, room.y + 1):
        action_adder(actions, 's', player.move_south, "Go South")
    if world.tile_at(room.x + 1, room.y):
        action_adder(actions, 'e', player.move_east, "Go East")
    if world.tile_at(room.x - 1, room.y):
        action_adder(actions, 'w', player.move_west, "Go West")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()
