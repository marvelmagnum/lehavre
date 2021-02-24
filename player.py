import resources
import math


class Player:
    def __init__(self, name, type):
        self.name = name    # player name: p1, p2, p3, ...
        self.inventory = {'money': 15, 'coal': 1}
        self.location = 'none'  # player's location: none, building names
        self.type = type    # player type: "human", "computer"

    @staticmethod
    def create_player(name):
        """ Create human or computer player """
        if name.lower() == "ai":
            return Player(name.upper(), 'computer')
        else:
            return Player(name.title(), 'human')

    def buy_buildings(self, game_state):
        """ Buy available buildings """
        while True:
            print("Select building to buy:")
            choices = []
            for i in range(0, 3):
                if game_state.stacks[i] and game_state.stacks[i][0].price > 0:
                    choices.append(game_state.stacks[i][0])
            for building in game_state.constructed:
                if building.owner == 'game' and building.price > 0:
                    choices.append(building)
            for idx, building in enumerate(choices):
                print(str(idx + 1) + '. ' + building.name.title() + ' - ' + str(building.price))
            print(str(idx + 2) + ". Nothing")
            ans = input("? ")
            if int(ans) == len(choices) + 1:
                break
            building = choices[int(ans) - 1]
            if building.price > self.inventory['money']:
                print("You cannot afford to purchase the " + building.name.title() + '.')
            else:
                self.inventory['money'] -= building.price
                building.owner = self
                if building not in game_state.constructed:
                    game_state.constructed.append(building)
                    for i in range(0, 3):
                        if game_state.stacks[i] and game_state.stacks[i][0] == building:
                            game_state.stacks[i].pop()
                if building.current_user != 'none':  # vacate building if anyone is using it
                    user = building.current_user
                    building.current_user = user.location = 'none'
                print("You purchased the " + building.name.title() + '.')
                break

    def sell_buildings(self, game_state):
        """ Sell owned buildings """
        choices = []
        for building in game_state.constructed:
            if building.owner == self:
                choices.append(building)
        if len(choices) == 0:
            print ("You do not own any buildings.")
            return
        while True:
            print("Select building to sell:")
            for idx, building in enumerate(choices):
                print(str(idx+1) + '. ' + building.name.title() + ' - ' + str(int(building.value / 2)))
            print(str(idx+2) + ". Nothing")
            ans = input("? ")
            if int(ans) == len(choices) + 1:
                break
            building = choices[int(ans)-1]
            self.inventory['money'] += int(building.value / 2)
            building.owner = 'game'
            if building.current_user != 'none': # vacate building if anyone is using it
                user = building.current_user
                building.current_user = user.location = 'none'
            print("You sold the " + building.name.title() + " for " + str(int(building.value / 2)) + " money.")
            break


    def buy_ships(self, game_state):
        """ Buy available ships """
        if not game_state.ships['game']['wooden'] and not game_state.ships['game']['iron'] and not game_state.ships['game']['steel']:
            print("There are presently no ships on sale.")
            return
        while True:
            print("Select ship to buy:")
            choices = []
            ''' add wooden, iron and steel ships on sale. liners cannot be bought. '''
            if game_state.ships['game']['wooden']:
                choices.append(game_state.ships['game']['wooden'][0])
            if game_state.ships['game']['iron']:
                choices.append(game_state.ships['game']['iron'][0])
            if game_state.ships['game']['steel']:
                choices.append(game_state.ships['game']['steel'][0])
            for idx, ship in enumerate(choices):
                print(str(idx + 1) + '. ' + ship.type.title() + ' "' + ship.name.title() + '" - ' + str(ship.price))
            print(str(idx + 2) + ". Nothing")
            ans = input("? ")
            if int(ans) == len(choices) + 1:
                break
            ship = choices[int(ans) - 1]
            if ship.price > self.inventory['money']:
                print('You cannot afford to purchase the "' + ship.name.title() + '".')
            else:
                self.inventory['money'] -= ship.price
                game_state.ships[self].append(ship)
                if ship.type == "wooden ship":
                    game_state.ships['game']['wooden'].pop()
                if ship.type == "iron ship":
                    game_state.ships['game']['iron'].pop()
                if ship.type == "steel ship":
                    game_state.ships['game']['steel'].pop()
                print("You purchased the " + ship.type.title() + ' "' + ship.name.title() + '".')
                break

    def sell_ships(self, game_state):
        """ Sell owned ships """
        if self not in game_state.ships or not game_state.ships[self]:
            print("You do not own any ships.")
            return
        while True:
            print("Select ship to sell:")
            for idx, ship in enumerate(game_state.ships[self]):
                print(str(idx+1) + '. ' + ship.type.title() + ' "' + ship.name.title() + '" - ' + str(int(ship.value / 2)))
            print(str(idx+2) + ". Nothing")
            ans = input("? ")
            if int(ans) == len(game_state.ships[self]) + 1:
                break
            ship = game_state.ships[self][int(ans)-1]
            self.inventory['money'] += int(ship.value / 2)
            game_state.ships[self].remove(ship)
            if ship.type == "wooden ship":
                game_state.ships['game']['wooden'].append(ship)
            if ship.type == "iron ship":
                game_state.ships['game']['iron'].append(ship)
            if ship.type == "steel ship":
                game_state.ships['game']['steel'].append(ship)
            print("You sold the " + ship.type.title() + ' "' + ship.name.title() + '" for ' + str(int(ship.value / 2)) + " money.")
            break


    def perform_buy(self, game_state):
        """ Additional player action - Buy """
        while True:
            print("Select item to buy ?")
            print("1. Buildings")
            print("2. Ships")
            print("3. Nothing")
            ans = input("? ")
            if int(ans) == 3:
                break
            elif int(ans) == 1:
                self.buy_buildings(game_state)
            elif int(ans) == 2:
                self.buy_ships(game_state)

    def perform_sell(self, game_state):
        """ Additional player action - Sell """
        while True:
            print("Select item to sell ?")
            print("1. Buildings")
            print("2. Ships")
            print("3. Nothing")
            ans = input("? ")
            if int(ans) == 3:
                break
            elif int(ans) == 1:
                self.sell_buildings(game_state)
            elif int(ans) == 2:
                self.sell_ships(game_state)

    def take_harvest(self):
        """ Gain harvest resources """
        grain = cattle = False
        if 'grain' in self.inventory and self.inventory['grain'] >= 1:
            self.inventory['grain'] += 1
            grain = True
        if 'cattle' in self.inventory and self.inventory['cattle'] >= 2:
            self.inventory['cattle'] += 1
            cattle = True
        if grain and cattle:
            print(self.name + " bred Cattle and harvested Grain.")
        elif grain:
            print(self.name + " harvested Grain.")
        elif cattle:
            print(self.name + " bred Cattle.")
        else:
            print(self.name + " did not produce Grain or Cattle.")

    def take_loan(self, food_req):
        """ Takes as many loans reqd """
        loan_count = int(math.ceil(food_req / 4))
        print("You will need loan to cover your food deficit of " + str(food_req) + ".")
        if 'loan' in self.inventory:
            self.inventory['loan'] += loan_count
        else:
            self.inventory['loan'] = loan_count
        self.inventory['money'] += loan_count * 4
        print("You take out " + str(loan_count) + " loans and receive " + str(loan_count * 4) + " money.")

    def repay_loan(self):
        """ Repay loans """
        max_repay = int(self.inventory['money'] / 5)
        print(
            "You can repay upto " + str(max_repay) + " of your total " + str(self.inventory['loan']) + " active loans.")
        while True:
            ans = input("Each loan will require 5 money to repay. How many do you want to repay ? ")
            if int(ans) <= max_repay:
                break
            print("You only have enough to repay " + str(max_repay) + " loans.")
        self.inventory['money'] -= int(ans) * 5
        self.inventory['loan'] -= int(ans)
        if self.inventory['loan'] == 0:
            print("You have repaid all active loans for " + str(int(ans) * 5) + " money.")
        else:
            print("You have repaid " + ans + " active loans for " + str(int(ans) * 5) + " money.")

    def handle_food_deficit(self, game_state, foodstuff, avail_food, food):
        """ Not enough food. sell property or take loan """
        print("You do not have enough food.")
        if avail_food > 0:
            for food_item, quantity in foodstuff:
                self.inventory[food_item.name] = 0
                print(str(quantity) + ' x ' + food_item.name.title() + '(' + str(food_item.food) + ' food) ', end="")
            print(" were consumed from your storage.")
            print("You still have " + str(food - avail_food) + " food deficit.")
        print("Your options:")
        print("1. Sell Buildings / Ships")
        print("2. Take Loan")
        ans = input("? ")
        if int(ans) == 1:  # sell property
            self.perform_sell(game_state)
        elif int(ans) == 2:  # take loan
            self.take_loan(food - avail_food)

    def get_avail_food(self):
        """ Return amount of food in inventory as well as a list of tuples for the food item resource and available qty.
            Ignores money as it can possibly be used in better ways. """
        foodstuff = []
        avail_food = 0
        for key, value in self.inventory.items():
            if resources.resource_map[key].food > 0 and self.inventory[key] > 0 and key != 'money':
                foodstuff.append((resources.resource_map[key], value))
                avail_food += resources.resource_map[key].food * self.inventory[key]
        return avail_food, foodstuff

    def feed(self, game_state, food):
        """ Handle feeding req at round ends """
        print(self.name + " needs to arrange for " + str(food) + " food.")
        while True:
            avail_food, foodstuff = self.get_avail_food()
            if (avail_food >= food):  # has enough food to feed
                print("You have:")
                idx = 1
                for food_item, quantity in foodstuff:
                    print(str(idx) + ". " + food_item.name.title() + ": " + str(quantity)
                          + " [" + str(food_item.food) + " food each]")
                    idx += 1
                ans = input("Select food to consume: ")
                entry = foodstuff[int(ans) - 1]
                num = input("How many: ")
                if int(num) <= entry[1]:
                    food -= entry[0].food * int(num)
                    print("You have consumed " + str(entry[0].food * int(num)) + ' ' + entry[0].name.title() + '. ',
                          end=" ")
                    self.inventory[entry[0].name] -= int(num)
                    if food <= 0:
                        print(self.name + " has successfully met the feeding requirement.")
                        break
                    else:
                        print("Need to consume " + str(food) + " more food.")
                else:
                    print("You don't have " + num + ' ' + entry[0].name.title())
            else:
                self.handle_food_deficit(game_state, foodstuff, avail_food, food)
                food -= avail_food

    def get_ship_food(self, game_state):
        """ Return amount of food generated from owned ships """
        pl_count = len(game_state.players)
        ship_food = 0
        if self in game_state.ships:
            for ship in game_state.ships[self]:
                ship_food += ship.food[pl_count-1]
                print(self.name + "'s " + ship.type + ', ' + ship.name.title() + ", brought in " + str(ship.food[pl_count - 1]) + " food.")
        return ship_food
