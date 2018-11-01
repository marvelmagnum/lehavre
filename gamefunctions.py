import gamestate
import resources


def get_entry_cost(building):
    """ Get the entry cost of a building """
    if not building.fees:
        return None # free
    print(building.name.title() + " usage fees: ", end = "")
    for key, value in building.fees.items():
        print(key.title() + ' [' + str(value) + '] ')
    for key, value in building.fees.items():
        if check_availability(key, value):
            return collect_cost(key, value)
        else:
            print ("You don't have enough " + key + ".")
            return None


def collect_cost(resource_type, amount):
    """ Collect food/money from player as fees """
    if resource_type == 'food':
        foodstuff = []
        for key,value in gamestate.game_state.inventory.items():
            if resources.resource_map[key].food > 0:
                foodstuff.append((resources.resource_map[key],value))
        print("You have:")
        idx = 1
        for food_item, quantity in foodstuff:
            print(str(idx) + ". " + food_item.name.title() + ": " + str(quantity)
                  + " [" + str(food_item.food) + " food each]")
            idx += 1
        chosen_fees = []
        while True:
            ans = input("Select food to give: ")
            if int(ans) > len(foodstuff):
                continue
            entry = foodstuff[int(ans)-1];
            num = input("How many: ")
            if int(num) <= entry[1]:
                amount -= entry[0].food * int(num)
                print("You have paid " + str(entry[0].food * int(num)) + ' ' + entry[0].name.title() + '. ', end=" ")
                chosen_fees.append((entry[0].name, int(num)))
                gamestate.game_state.inventory[entry[0].name] -= int(num)
                if amount <= 0:
                    print()
                    return chosen_fees
                else:
                    print("Need to pay " + str(amount) + " more food.")
            else:
                print("You don't have " + num + ' ' + entry[0].name.title())
    elif resource_type == 'energy':
        energy_stuff = []
        for key,value in gamestate.game_state.inventory.items():
            if resources.resource_map[key].energy > 0:
                energy_stuff.append((resources.resource_map[key],value))
        print("You have:")
        idx = 1
        for energy_item, quantity in energy_stuff:
            print(str(idx) + ". " + energy_item.name.title() + ": " + str(quantity)
                  + " [" + str(energy_item.energy) + " energy each]")
            idx += 1
        chosen_fees = []
        while True:
            ans = input("Select energy to spend: ")
            if int(ans) > len(energy_stuff):
                continue
            entry = energy_stuff[int(ans)-1];
            num = input("How many: ")
            if int(num) <= entry[1]:
                amount -= entry[0].energy * int(num)
                print("You have spent " + str(int(num)) + ' ' + entry[0].name.title() + '. ', end=" ")
                chosen_fees.append((entry[0].name, int(num)))
                gamestate.game_state.inventory[entry[0].name] -= int(num)
                if amount <= 0:
                    print()
                    return chosen_fees
                else:
                    print("Need to spend " + str(amount) + " more energy.")
            else:
                print("You don't have " + num + ' ' + entry[0].name.title())
    elif resource_type == 'money':
        chosen_fees = []
        print("You have " + str(gamestate.game_state.inventory['money']) + " money. Pay " + str(amount) + " ?")
        print("1. Yes")
        print("2. No")
        ans = input("? ")
        if int(ans) == 1:
            chosen_fees.append(('money', amount))
            gamestate.game_state.inventory['money'] -= amount
            return chosen_fees
        else:
            return None


def check_availability(resource_type, amount):
    """ Check if the required fees are available with the player """
    if resource_type == 'food':
        for key,value in gamestate.game_state.inventory.items():
            amount -= resources.resource_map[key].food * value
            if amount <= 0:
                return True
        return False
    elif resource_type == 'energy':
        for key, value in gamestate.game_state.inventory.items():
            amount -= resources.resource_map[key].energy * value
            if amount <= 0:
                return True
        return False
    elif resource_type == 'money':
        if gamestate.game_state.inventory['money'] >= amount:
            return True
        else:
            return False




def occupy_building(building):
    """ current player occupied building. free building occupied by player previously """
    building_name = gamestate.game_state.location[gamestate.game_state.current_player]
    for b in gamestate.game_state.constructed:
        if b.name == building_name:
            b.current_user = 'none'
    building.current_user = gamestate.game_state.current_player
    gamestate.game_state.location[gamestate.game_state.current_player] = building.name
