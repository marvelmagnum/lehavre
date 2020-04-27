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
    """ Perform Feeding Phase """
    pl_count = len(game_state.players)
    for player in game_state.players:
        if player.type == 'computer':
            continue
        if player in game_state.ships:
            ship_food = 0
            for ship in game_state.ships[player]:
                ship_food += ship.food[pl_count]
                print (player.name + "'s " + ship.type + ', ' + ship.name.title() + ", brought in " + str(ship.food[pl_count]) + " food.")
                food_req -= ship_food
        if food_req > 0:
            player.feed(game_state, food_req)


def develop_town(game_state, development_type):
    """ Handles town development at round end """
    ''' TODO: Handle special and standard buildings separately when added to game '''
    if development_type == 'standard' or development_type == 'special':
        priority = 1000
        building = 'none'
        idx = -1
        for i in range(0,3):
            if game_state.stacks[i]:
                if game_state.stacks[i][0].rank < priority:
                    priority = game_state.stacks[i][0].rank
                    building = game_state.stacks[i][0]
                    idx = i
        building.owner = 'game'
        game_state.constructed.append(building)
        game_state.stacks[idx].pop()
        print ("City has completed construction of the " + building.name.title())


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
    if ship_card.harvest[pl_count][3] != 'none':
        develop_town(game_state, ship_card.harvest[pl_count][3])
    else:
        print("No Town Development this round.")
    ''' new ship '''
    print("A new ", end="")
    if ship_card.type == 'wooden ship':
        game_state.ships['game']['wooden'].append(ship_card)
        print(ship_card.type.title() + ' "' + ship_card.name.title() + '" ', end="")
    elif ship_card.type == 'iron ship':
        game_state.ships['game']['iron'].append(ship_card)
        print(ship_card.type.title() + ' "' + ship_card.name.title() + '" ', end="")
    elif ship_card.type == 'steel ship':
        game_state.ships['game']['steel'].append(ship_card)
        print(ship_card.type.title() + ' "' + ship_card.name.title() + '" ', end="")
    elif ship_card.type == 'luxury liner':
        game_state.ships['game']['liner'].append(ship_card)
        print(ship_card.type.title() + ' "' + ship_card.name.title() + '" ', end="")
    print("is now available for sale.")


def pay_interest(game_state):
    """ Collect interest from players who have 1 or more loans """
    ''' TODO: AI need to autonomously choose between paying interest of repaying loan based on its strategy.'''
    loan_count = 0
    for player in game_state.players:
        if 'loan' in player.inventory and player.inventory['loan'] > 0:
            if player.inventory['money'] >= 5:   # option to repay loan
                print(player.name + " can repay active loans or pay interest.")
                print("1. Repay Loan")
                print("2. Pay Interest")
                while True:
                    ans = input("? ")
                    if int(ans) == 1:
                        player.repay_loan()
                        break
                    if int(ans) == 2:
                        break;

            if player.inventory['loan'] > 0:
                if player.inventory['money'] > 0:
                    player.inventory['money'] -= 1
                else:
                    player.inventory['loan'] += 1
                    player.inventory['money'] += 3
                    print(player.name + " had to take a loan. Received 4 money.")
                print(player.name + " pays 1 money towards loan interest.")
                loan_count += 1

    if loan_count == 0:
        print("Nobody has any active loans.")
