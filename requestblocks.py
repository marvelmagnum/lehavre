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
            if len(blueprint.build_cost) == 0:
                print("N/A ]")
            else:
                for key, value in blueprint.build_cost.items():
                    print(key.title() + "(" + str(value) + ")", end=" ")
                print(']')
            idx += 1
        sel = input("? ")
        return game_state.blueprints[int(sel)-1]


class SelectInventoryItems:
    """ Gets dictionary of items from inventory (except money) """

    def get(self, game_state):
        if len(game_state.inventory) == 0:
            return None
        inv_menu = []
        for key, value in game_state.inventory.items():
            if value > 0 and key != 'money':
                inv_menu.append((key,value))
        selected = {}
        while (True):
            print("Select items from inventory:")
            idx = 1
            for item, quantity in inv_menu:
                print(str(idx) + '. ' + item.title() + ": " + str(quantity))
                idx += 1
            sel = input("Item number ? ")
            num = input("You got " + str(inv_menu[int(sel)-1][1]) + ' '
                        + inv_menu[int(sel)-1][0].title() + ". How many ? ")
            if int(num) > inv_menu[int(sel)-1][1]:
                print("You don't have that much.")
                continue
            if inv_menu[int(sel)-1][0] in selected:
                selected[inv_menu[int(sel)-1][0]] += int(num)
            else:
                selected[inv_menu[int(sel) - 1][0]] = int(num)
            stuff = inv_menu[int(sel)-1][0]
            qty = inv_menu[int(sel)-1][1] - int(num)
            inv_menu[int(sel)-1] = (stuff, qty)
            if inv_menu[int(sel)-1][1] <= 0:
                del inv_menu[int(sel)-1]
            print("Selection: ", end="")
            for key, value in selected.items():
                if value > 0:
                    print("[ " + key.title() + ": " + str(value) + " ]", end="")
            print()
            if len(inv_menu) <= 0:
                break;
            print("More ?")
            print("1. Yes")
            print("2. No")
            ans = input("? ")
            if int(ans) != 1:
                break
        return selected


class SelectPlayer:
    """ Gets current player """
    def get(self, game_state):
        return game_state.current_player


class GetEmptyOffers:
    """ Gets list of items whose offers are empty """
    def get(self, game_state):
        empty_offers = []
        for key, value in game_state.offers.items():
            if value == 0:
                empty_offers.append(key)
        return empty_offers


class SetTradeRequest:
    """ Selects an item among 'choices' and specified amount for trading """
    choices = []

    def __init__(self, choices):
        self.choices = choices

    def get(self, game_state):
        if len(self.choices) == 1:
            print("Trade " + self.choices[0].title() + " ? ")
            print("1. Yes")
            print("2. No")
            ans = input("? ")
            if int(ans) == 2:
                return self.choices[0], 0
            qty = input("How many " + self.choices[0].title() + " do you want ? ")
            return self.choices[0], int(qty)
        if len(self.choices) > 1:
            print("Select commodity to trade:")
            for idx, item in enumerate(self.choices):
                print(str(idx+1) + ". " + item.title())
            print(str(idx+2) + ". Nothing")
            ans = input("? ")
            if int(ans) == idx+2:
                return self.choices[int(ans)-2], 0
            qty = input("How many " + self.choices[int(ans)-1].title() + " do you want ? ")
            return self.choices[int(ans)-1], int(qty)
