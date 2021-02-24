import gamefunctions

class GetQuantity:
    """ Gets quantity of an 'item' type """
    def __init__(self, item, limit = 0):
        self.item = item
        self.limit = limit

    def get(self, game_state):
        qty = int(input("How many " + self.item.title() + ": "))
        while self.limit > 0 and qty > self.limit:
            qty = int(input("Limit is " + str(self.limit) + " " + self.item.title() + ". Re-enter: "))
        return qty


class SelectBlueprint:
    """ Gets a building from the available blueprints. setting 'reqc_item' only allows selection of blueprints that require it. """
    def __init__(self, item = 'undefined'):
        self.reqd_item = item

    def get(self, game_state):
        if len(game_state.blueprints) == 0:
            return None

        print("Select building to construct", end="")
        if self.reqd_item != 'undefined':
            print(" (must require " + self.reqd_item.title() + "):")
        else:
            print(":")

        available = []
        for i in range(0,3):
            if game_state.stacks[i]:
                available.append(game_state.stacks[i][0])

        idx = 1
        for blueprint in available:
            print(str(idx) + ": " + blueprint.name.title(), end=" [ ")
            if len(blueprint.build_cost) == 0:
                print("N/A ]")
            else:
                for key, value in blueprint.build_cost.items():
                    print(key.title() + "(" + str(value) + ")", end=" ")
                print(']')
            idx += 1
        while (True):
            sel = input("? ")
            if self.reqd_item != 'undefined' and self.reqd_item not in available[int(sel)-1].build_cost.keys():
                print ("Building must require " + self.reqd_item.title() + " to construct. Select again.")
                continue
            elif int(sel) > idx - 1:
                print ("Invalid selection.")
                continue
            elif len(available[int(sel)-1].build_cost) == 0:
                print (available[int(sel)-1].name.title() + " is an un-buildable building. May only be purchased.")
            else:
                return available[int(sel)-1]


class SelectShipType:
    """ Gets a ship from the available ships. """

    def get(self, game_state):
        if len(game_state.ships['game']) == 0:
            return None

        print("Select ship to build:")
        for idx, ship in enumerate(game_state.ships['game']):
            print(str(idx+1) + ": " + ship.name.title() + '[' + ship.type.title() + ']', end=" : ")
            for key, value in ship.build_cost.items():
                print(key.title() + "(" + str(value) + ")", end=" ")
            print("Energy(3)")
        sel = input("? ")
        return game_state.ships['game'][int(sel) - 1]


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


class GetExchangeRequest:
    """ Sets up 'options' for a specific 'item' for exchange """
    def __init__(self, item, options):
        self.item = item
        self.options = options

    def get(self, game_state):
        print("How many " + self.item.title() + " ? ")
        for idx, opt in enumerate(self.options):
            print(str(idx+1) + ". " + str(opt))
        sel = input("? ")
        return self.item, self.options[int(sel)-1], int(sel)-1


class GetShipment:
    """ Setup player ships with consignment and reserve fuel """

    def get(self, game_state):
        total_ships = len(game_state.ships[game_state.current_player]);
        if total_ships == 0:
            print("You do not have any ships.")
            return None

        print("You have " + str(total_ships) + " ship(s).")
        for idx, ship in enumerate(game_state.ships[game_state.current_player]):
            print(str(idx+1) + ". " + ship.type.title() + ' "' + ship.name.title() + '" [ Capacity: ' + str(ship.capacity) + "]")
        scount = total_ships
        fuel_check = gamefunctions.check_availability('energy', scount * 3)
        while fuel_check == False:
            scount -= 1
            if scount == 0:
                break;
            fuel_check = gamefunctions.check_availability('energy', scount * 3)
        if scount == 0:
            print("You do not have any energy to fuel ship.")
            return None

        print("You can fuel " + str(scount) + " ship(s). Each ship requires 3 energy to ship goods.")
        count = input("How many ships do you want to fuel ? (Fuels your best ships first): ")
        while int(count) > scount:
            count = input("You only have enough Energy to fuel " + str(scount) + " ships. Re-enter: ")

        selected_ships = []
        available_ships = game_state.ships[game_state.current_player]
        num = 0
        while num < int(count):
            best_cargo = 0
            chosen_ship = None
            for ship in available_ships:
                if ship.capacity > best_cargo:
                    chosen_ship = ship
                    best_cargo = ship.capacity
            selected_ships.append(chosen_ship)
            available_ships.remove(chosen_ship)
            num += 1

        energy_reqd = 0
        num_goods = 0
        for ship in selected_ships:
            energy_reqd += ship.fuel['energy']
            num_goods += ship.capacity
        print("You need " + str(energy_reqd) + " to fuel your " + str(count) + " ship(s).")
        gamefunctions.collect_cost('energy', energy_reqd)

        print("You can now ship " + str(num_goods) + " goods.")

        inv_menu = []
        for key, value in game_state.inventory.items():
            if value > 0 and key != 'money':
                inv_menu.append((key,value))
        selected = {}
        while (True):
            print("Select items to ship:")
            idx = 1
            for item, quantity in inv_menu:
                print(str(idx) + '. ' + item.title() + ": " + str(quantity))
                idx += 1
            sel = input("Item number ? ")
            if int(sel) >= idx:
                print("Invalid input. Please select again.")
                continue
            num = input("You got " + str(inv_menu[int(sel)-1][1]) + ' '
                        + inv_menu[int(sel)-1][0].title() + ". How many ? ")
            if int(num) > inv_menu[int(sel)-1][1]:
                print("You don't have that much.")
                continue
            if int(num) > num_goods:
                print("Cannot load " + num + " " + inv_menu[int(sel)-1][0].title() + ". Available shipping capacity is " + str(num_goods) + " items.")
                continue
            if inv_menu[int(sel)-1][0] in selected:
                selected[inv_menu[int(sel)-1][0]] += int(num)
            else:
                selected[inv_menu[int(sel) - 1][0]] = int(num)
            stuff = inv_menu[int(sel)-1][0]
            qty = inv_menu[int(sel)-1][1] - int(num)
            num_goods -= int(num)
            print(num + " " + stuff.title() + " was loaded. ", end="")
            if num_goods > 0:
                print("Available shipping capacity is " + str(num_goods) + " items.")
            else:
                print("Your ship(s) have been fully loaded.")
            inv_menu[int(sel)-1] = (stuff, qty)
            if inv_menu[int(sel)-1][1] <= 0:
                del inv_menu[int(sel)-1]
            print("Shipment: ", end="")
            for key, value in selected.items():
                if value > 0:
                    print("[ " + key.title() + ": " + str(value) + " ]", end="")
            print()
            if len(inv_menu) <= 0:
                break;
            if num_goods <= 0:
                break;

        return selected_ships, selected



