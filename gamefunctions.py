import resources


def get_entry_cost(game_state, building):
    """ Get the entry cost of a building """
    if not building.fees:
        return None # free
    print(building.name.title() + " usage fees: ", end="")
    if len(building.fees) == 1:
        for key, value in building.fees[0].items():
            print(key.title() + ' [' + str(value) + '] ')
        for key, value in building.fees[0].items():
            if check_availability(game_state, key, value):
                return collect_cost(game_state, key, value)
            else:
                print ("You don't have enough " + key + ".")
                return None
    else:
        print()
        for idx, fee_entry in enumerate(building.fees):
            for key, value in fee_entry.items():
                print(str(idx+1) + ". " + key.title() + ' [' + str(value) + '] ')
        opt = input("Select an option: ")
        for key, value in building.fees[int(opt)-1].items():
            if check_availability(game_state, key, value):
                return collect_cost(game_state, key, value)
            else:
                print ("You don't have enough " + key + ".")
                return None


def collect_cost(game_state, resource_type, amount):
    """ Collect food/money from player as fees """
    if resource_type == 'food':
        foodstuff = []
        for key,value in game_state.current_player.inventory.items():
            if resources.resource_map[key].food > 0 and game_state.current_player.inventory[key] > 0:
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
                game_state.current_player.inventory[entry[0].name] -= int(num)
                if amount <= 0:
                    print()
                    return chosen_fees
                else:
                    print("Need to pay " + str(amount) + " more food.")
            else:
                print("You don't have " + num + ' ' + entry[0].name.title())
    elif resource_type == 'energy':
        energy_stuff = []
        for key,value in game_state.current_player.inventory.items():
            if resources.resource_map[key].energy > 0 and game_state.current_player.inventory[key] > 0:
                energy_stuff.append((resources.resource_map[key],value))
        print("You have:")
        idx = 1
        for energy_item, quantity in energy_stuff:
            print(str(idx) + ". " + energy_item.name.title() + ": " + str(quantity)
                  + " [" + str(energy_item.energy) + " energy each]")
            idx += 1
        chosen_fees = []
        while True:
            ans = input("Select item to use for energy: ")
            if int(ans) > len(energy_stuff):
                continue
            entry = energy_stuff[int(ans)-1]
            num = input("How many: ")
            if int(num) <= entry[1]:
                amount -= entry[0].energy * int(num)
                print("You have spent " + str(int(num)) + ' ' + entry[0].name.title() + '. ', end=" ")
                chosen_fees.append((entry[0].name, int(num)))
                game_state.current_player.inventory[entry[0].name] -= int(num)
                if amount <= 0:
                    print()
                    return chosen_fees
                else:
                    print("Need to spend " + str(amount) + " more energy.")
            else:
                print("You don't have " + num + ' ' + entry[0].name.title())
    elif resource_type == 'money':
        chosen_fees = []
        print("You have " + str(game_state.current_player.inventory['money']) + " money. Pay " + str(amount) + " ?")
        print("1. Yes")
        print("2. No")
        ans = input("? ")
        if int(ans) == 1:
            chosen_fees.append(('money', amount))
            game_state.current_player.inventory['money'] -= amount
            return chosen_fees
        else:
            return None


def check_availability(game_state, resource_type, amount):
    """ Check if the required fees are available with the player """
    if resource_type == 'food':
        for key,value in game_state.current_player.inventory.items():
            amount -= resources.resource_map[key].food * value
            if amount <= 0:
                return True
        return False
    elif resource_type == 'energy':
        for key, value in game_state.current_player.inventory.items():
            amount -= resources.resource_map[key].energy * value
            if amount <= 0:
                return True
        return False
    elif resource_type == 'money':
        if game_state.current_player.inventory['money'] >= amount:
            return True
        else:
            return False


def occupy_building(game_state, building):
    """ current player occupied building. free building occupied by player previously """
    prev_location = game_state.current_player.location
    for b in game_state.constructed:
        if b.name == prev_location:
            b.current_user = 'none'
    building.current_user = game_state.current_player
    game_state.current_player.location = building.name


def do_harvest(game_state):
    """ Perform Harvest Phase """
    for player in game_state.players:
        player.take_harvest()


def perform_feeding(game_state, food_req):
    """ Perform Feeding Phase"""
    pl_count = len(game_state.players)
    for player in game_state.players:
        if player in game_state.ships:
            ship_food = 0
            for ship in game_state.ships[player]:
                ship_food += ship.food[pl_count]
                print (player.name + "'s " + ship.type + ', ' + ship.name.title() + ", brought in " + str(ship.food[pl_count]) + " food.")
                food_req -= ship_food
        if food_req > 0:
            player.feed(food_req)


def round_end(game_state):
    """ End of round bookkeeping """
    ship_card = game_state.harvest.pop()
    pl_count = len(game_state.players)

    ''' harvest phase if available '''
    if ship_card.harvest[pl_count][1] == True:
        print("Harvest Phase")
        do_harvest(game_state)
    else:
        print("No Harvest this round.")

    ''' feeding phase '''
    print("Feeding Phase")
    print("Players need to satisfy the feeding requirement of " + str(ship_card.harvest[pl_count][2]) + " food.")
    perform_feeding(game_state, ship_card.harvest[pl_count][2])

    ''' town building phase '''
    ''' new ship '''

