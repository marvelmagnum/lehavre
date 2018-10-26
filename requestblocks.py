class GetQuantity:
    """ Gets quantity of an 'item' type """
    item = "undefined"

    def __init__(self, item):
        self.item = item

    def get(self, game_state):
        return int(input("How many " + self.item + ": "))


class SelectBlueprint:
    """ Gets a building from the available blueprints """
    def get(self, game_state):
        if len(game_state.blueprints) == 0:
            return None
        print("Select building to construct:")
        idx = 1
        for blueprint in game_state.blueprints:
            print(str(idx) + ": " + blueprint.name.title(), end=" [ ")
            for key, value in blueprint.build_cost.items():
                print(key.title() + "(" + str(value) + ")", end=" ")
            print(']')
            idx += 1
        sel = input("? ")
        return game_state.blueprints[int(sel)-1]


class SelectPlayer:
    """ Gets current player """
    def get(self, game_state):
        return game_state.current_player

