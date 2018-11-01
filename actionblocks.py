import math
import gamefunctions
import resources

class RemoveItems:
    """ Removes 'item' type from inventory applying the 'modifier' """
    item = "undefined"
    modifier = 0.0

    def __init__(self, item, mod):
        self.item = item
        self.modifier = mod

    '''args: 0 = game_state, 1 = amt'''
    def do(self, args):
        if self.item in args[0].inventory and args[0].inventory[self.item] >= args[1]:
            args[0].inventory[self.item] -= args[1] * self.modifier
            return True
        else:
            print("You don't have " + str(args[1]) + ' ' + self.item.title())
            return False


class AddItems:
    """ Adds 'item' type to inventory applying the 'modifier' """
    item = "undefined"
    modifier = 0.0

    def __init__(self, item, mod):
        self.item = item
        self.modifier = mod

    '''args: 0 = game_state, 1 = amt'''
    def do(self, args):
        if self.item in args[0].inventory:
            args[0].inventory[self.item] += int(args[1] * self.modifier)
        else:
            args[0].inventory[self.item] = int(args[1] * self.modifier)
        return True


class ReceiveItems:
    """ Adds 'item' type to inventory in the specified 'quantity'. Adds 'bonus' amt for 'icons' """
    item = "undefined"
    quantity = 0
    icon = "none"
    bonus = 0

    def __init__(self, item, qty, icon = 'none', bonus = 0):
        self.item = item
        self.quantity = qty
        self.icon = icon
        self.bonus = bonus

    '''args: 0 = game_state, 1 = player'''
    def do(self, args):
        if self.item in args[0].inventory:
            args[0].inventory[self.item] += self.quantity
        else:
            args[0].inventory[self.item] = self.quantity
        print("You received " + str(self.quantity) + " " + self.item.title(), end="")
        if self.icon != 'none':
            count = 0
            for building in args[0].constructed:
                if args[1] == building.owner:
                    for ic in building.icon:
                        if ic == self.icon:
                            count += 1
                            break
            total = self.bonus * count
            if total > 0:
                args[0].inventory[self.item] += total
                print(" and an additional " + str(total) + " " + self.item.title() + " for your " + self.icon.title() + " buildings.")
            else:
                print(".")
        return True


class Construct:
    """ Builds a blueprint, moves it to constructed, adds owner, deducts build cost applying the 'discount' """
    discounts = {'item' : 0}

    def __init__(self, discounts):
        self.discounts = discounts

    '''args: 0 = game state, 1 = building, 2 = owner'''
    def do(self, args):
        if args[1] is None:
            print("No blueprints available to construct.")
            return False
        if len(args[1].build_cost) == 0:
            print(args[1].name.title() + " can only be purchased. Cannot be built.")
            return False
        for key, value in args[1].build_cost.items():
            required = value
            for discount_key, discount_value in self.discounts.items():
                if key == discount_key:
                    required = value - discount_value
                    break
            if key in args[0].inventory and args[0].inventory[key] >= required:
                args[0].inventory[key] -= required
            else:
                print("You don't have enough " + key.title())
                return False
        args[1].owner = args[2]
        idx = 0
        while idx < len(args[0].blueprints):
            if args[0].blueprints[idx].name == args[1].name:
                break;
            idx += 1
        args[0].constructed.append(args[0].blueprints.pop(idx))
        return True


class CollectTickets:
    """ Collect 'amount' money per each player using owned buildings """
    amount = 0

    def __init__(self, amt):
        self.amount = amt

    '''args: 0 = game state, 1 = owner '''
    def do(self, args):
        visitors = 0
        for building in args[0].constructed:
            if building.owner == args[1]:
                if building.current_user != 'none' and building.current_user != args[1]:
                    visitors += 1
        if visitors > 0:
            args[0].inventory['money'] += visitors * self.amount
            print("You have " + str(visitors) + " visitors. Received " + str(visitors * self.amount) + " money.")
            return True
        else:
            print("You have no visitors at this time.")
            return False


class SpendEnergy:
    """ Removes chosen energy item from inventory applying the 'modifier' """
    modifier = 0.0

    def __init__(self,  mod):
        self.modifier = mod

    '''args: 0 = game_state, 1 = amt'''
    def do(self, args):
        required = math.ceil(args[1] * self.modifier)
        print(str(required) + " Energy required.")
        if gamefunctions.check_availability('energy', required):
            gamefunctions.collect_cost('energy', required)
            return True
        else:
            print("You don't have enough Energy.")
            return False


class CollectEmptyOffers:
    """ Adds 'quantity' of each item from empty offers to inventory """
    quantity = 0.0

    def __init__(self,  qty):
        self.quantity = qty

    '''args: 0 = game_state, 1 = empty offers'''
    def do(self, args):
        if len(args[1]) == 0:
            print("No empty offers to avail.")
            return False
        print("You received ", end="")
        for idx, offer in enumerate(args[1]):
            if offer in args[0].inventory:
                args[0].inventory[offer] += self.quantity
            else:
                args[0].inventory[offer] = self.quantity
            if len(args[1]) > 1 and idx < len(args[1])-2:
                print(offer.title(), end=', ')
            else:
                if len(args[1]) == 1 or idx == len(args[1])-2:
                    print(offer.title(), end=' ')
                else:
                    print("and " + offer.title(), end=' ')
        if len(args[1]) == 1:
            print ("[2]")
        else:
            print("[2 each]")
        return True


class SellItems:
    """ Sells items from inventory based on the 'standard_rate' and 'upgraded_rate' based on item category """
    standard_rate = 0
    upgraded_rate = 0

    def __init__(self, std_rate, upg_rate):
        self.standard_rate = std_rate
        self.upgraded_rate = upg_rate

    '''args: 0 = game_state, 1 = selected items from inventory'''
    def do(self, args):
        if len(args[1]) == 0:
            return False
        std_items = []
        std_count = 0
        upg_items = []
        upg_count = 0
        for key, value in args[1].items():
            if resources.resource_map[key].category == 'standard':
                std_count += value
                std_items.append(key)
            if resources.resource_map[key].category == 'upgraded':
                upg_count += value
                upg_items.append(key)
            args[0].inventory[key] -= value
        if std_count > 0:
            print("Sold " + str(std_count) + " standard items (", end="")
            for idx, sitem in enumerate(std_items):
                if len(std_items) == 1 or idx == len(std_items) - 1:
                    print(sitem.title(), end="")
                else:
                    print(sitem.title(), end=", ")
            print("). Value = " + str(math.floor(std_count / self.standard_rate)) + " Money")
        if upg_count > 0:
            print("Sold " + str(upg_count) + " upgraded items (", end="")
            for idx, uitem in enumerate(upg_items):
                if len(upg_items) == 1 or idx == len(upg_items) - 1:
                    print(uitem.title(), end="")
                else:
                    print(uitem.title(), end=", ")
            print("). Value = " + str(math.floor(upg_count / self.upgraded_rate)) + " Money")
        total = math.floor(std_count / self.standard_rate) + math.floor(upg_count / self.upgraded_rate)
        print("Received a total of " + str(total) + " Money")
        args[0].inventory['money'] += total
        return True

# TODO:: Fix a bug where a usage fees will be refunded if there are more than 1 TradeItem actions and any one of them fails.
class TradeItems:
    """ Trades items based on the trade rates set: the 'offer package' has a list of tuples (item and rate)
        'trade package' has a list of tradeable items corresponding to the package """

    offer_package = []
    trade_package = []

    def __init__(self, offer_package, trade_package):
        self.offer_package = offer_package
        self.trade_package = trade_package

    '''args: 0 = game_state, 1 = tuple of requested 'trade item' and 'quantity' desired'''
    def do(self, args):
        for idx, arg in enumerate(args):
            if idx == 0:
                continue
            if arg[0] in self.trade_package:
                request_param = args[idx]
                break
        if request_param[1] == 0:
            return True
        trade_item = request_param[0]
        trade_amount = request_param[1]
        required_items = {}
        for item_tuple in self.offer_package:
            required_items[item_tuple[0]] = trade_amount * item_tuple[1]
        inv_menu = []
        for ikey, ivalue in args[0].inventory.items():
            if ivalue > 0 and ikey != 'money':
                inv_menu.append((ikey, ivalue))
        for key, value in required_items.items():
            if key == 'any':
                current_given = value
                while True:
                    print("You have:")
                    idx = 1
                    total_inv = 0
                    for ikey, ivalue in inv_menu:
                        print(str(idx) + ". " + ikey.title() + ": " + str(ivalue))
                        total_inv += ivalue
                        idx += 1
                    if total_inv < current_given:
                        print ("You don't have enough goods to trade " + trade_item.title() + ".")
                        return False
                    sel = input("You need to give any " + str(current_given) + " goods for " + trade_item.title() + ". Select item ? ")
                    while True:
                        num = input("You got " + str(inv_menu[int(sel) - 1][1]) + ' '
                                    + inv_menu[int(sel) - 1][0].title() + ". How many ? ")
                        if int(num) > inv_menu[int(sel) - 1][1]:
                            print("You don't have that much.")
                            continue
                        stuff = inv_menu[int(sel) - 1][0]
                        qty = inv_menu[int(sel) - 1][1] - int(num)
                        current_given -= int(num)
                        print("You gave " + num + " " + inv_menu[int(sel) - 1][0].title() + ". ", end="")
                        if qty > 0:
                            inv_menu[int(sel) - 1] = (stuff, qty)
                        else:
                            del inv_menu[int(sel) - 1]
                        break
                    if current_given <= 0:
                        print()
                        break
                    else:
                        print("You need to give " + str(current_given) + " more goods.")
            else:
                idx = 0
                for ikey, ivalue in inv_menu:
                    if ikey == key:
                        if ivalue < value:
                            print("You don't have enough " + key.title() + " to trade for " + trade_item.title() + ".")
                            return False
                        print("You have " + str(ivalue) + " " + key.title() + ". Give " + str(value) + " ?")
                        print("1. Yes")
                        print("2. No")
                        ans = input("? ")
                        if int(ans) == 1:
                            stuff = inv_menu[idx][0]
                            qty = inv_menu[idx][1] - value
                            inv_menu[idx] = (stuff, qty)
                            print("You gave " + str(value) + " " + key.title() + ".")
                            break
                        else:
                            return False
                    idx += 1
        money = args[0].inventory['money']
        args[0].inventory = {'money' : money}
        for item, qty in inv_menu:
            args[0].inventory[item] = qty
        if trade_item in args[0].inventory:
            args[0].inventory[trade_item] += trade_amount
        else:
            args[0].inventory[trade_item] = trade_amount
        print("You received " + str(trade_amount) + " " + trade_item.title() + " through trading.")
        return True


class CheckResources:
    """ Check if the 'resources' are available with the player in the specified 'quantity'"""
    resources = {'item' : 0}

    def __init__(self, resource_list):
        self.resources = resource_list

    '''args: 0 = game_state'''
    def do(self, args):
        for key, value in self.resources.items():
            if key in args[0].inventory:
                if args[0].inventory[key] < value:
                    print("You don't have enough " + key.title())
                    return False
            else:
                print("You don't have any " + key.title())
                return False
        return True