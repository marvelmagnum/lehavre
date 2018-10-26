import math
import gamefunctions


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
        for key, value in args[1].build_cost.items():
            required = value
            for discount_key, discount_value in self.discounts.items():
                if key == discount_key:
                    required = value - discount_value
                    break
            if key in args[0].inventory and args[0].inventory[key] >= required:
                args[0].inventory[key] -= required
            else:
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
