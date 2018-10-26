import requestblocks
import actionblocks


class Building:
    name = "undefined"
    build_cost = {'item' : -1}
    fees = {'item' : -1}
    rank = 0
    value = 0
    price = 0   # for buildings which has different purchase cost than value. otherwise equal to value
    type = "none" # types: none, craftsman, economic, industrial, public
    icon = "none" # icons: none, hammer, fisherman
    owner = "undefined" # owners: blueprint, game, p1, p2, ...
    current_user = "none"  #users: none, p1, p2, ...
    usage_limit = 0
    description = "blah blah blah"

    ''' 
    requests: a list of request objects to get the use params for the building. 
    the objects are executed sequentially generating a list of args that is passed back
    
    actions: a list of action objects to create the effect of the card
    each object returns a true / false and are called in order. 
    If any object returns False, the card is unusable by player
    '''
    requests = []   # request  objects: these create a list of params passed on to the action objects
    actions = []    # action objects

    def ask(self, game_state):
        params = [game_state]       # first element is the game state
        for request in self.requests:
            params.append(request.get(game_state))  # returned values from the request objects are appended
        return params

    def use(self, args):
        for action in self.actions:
            if not action.do(args):  # list of params generated from requests
                return False         # action failed. any action failure usually means the building use failed
        return True           # building used normally


construction_firm = Building()
construction_firm.name = "construction firm"
construction_firm.build_cost = {}
construction_firm.fees = {'food' : 2}
construction_firm.rank = 0
construction_firm.value = construction_firm.price = 8
construction_firm.type = "industrial"
construction_firm.icon = "hammer"
construction_firm.owner = "game"
construction_firm.usage_limit = 2
construction_firm.description = "Build up to 2 buildings from the available blueprints."
get_blueprint = requestblocks.SelectBlueprint()
get_player = requestblocks.SelectPlayer()
construction_firm.requests = [get_blueprint, get_player]
build = actionblocks.Construct({})
construction_firm.actions = [build]

''' A '''
abattoir = Building()
abattoir.name = "abattoir"
abattoir.build_cost = {'wood' : 1, 'clay' : 1, 'iron' : 1}
abattoir.fees = {'money' : 2}
abattoir.rank = 9
abattoir.value = abattoir.price = 8
abattoir.type = "craftsman"
abattoir.icon = "none"
abattoir.owner = "blueprint"
abattoir.usage_limit = 1
abattoir.description = "Slaughter Cattle for Meat. Also receive 1 Hides for every 2 Cattle slaughtered."
get_quantity = requestblocks.GetQuantity('cattle')
abattoir.requests = [get_quantity]
give_cattle = actionblocks.RemoveItems('cattle', 1)
get_meat = actionblocks.AddItems('meat',1)
get_hide = actionblocks.AddItems('hides',0.5)
abattoir.actions = [give_cattle, get_meat, get_hide]

arts_center = Building()
arts_center.name = "arts center"
arts_center.build_cost = {'wood': 1, 'clay': 1}
arts_center.fees = {'food' : 1}
arts_center.rank = 11
arts_center.value = arts_center.price = 10
arts_center.type = "craftsman"
arts_center.icon = "fisherman"
arts_center.owner = "blueprint"
arts_center.usage_limit = 1
arts_center.description = "Receive 4 Money for each player using your buildings."
get_player = requestblocks.SelectPlayer()
arts_center.requests = [get_player]
collect_tickets = actionblocks.CollectTickets(4)
arts_center.actions = [collect_tickets]

''' B '''
bakehouse = Building()
bakehouse.name = "bakehouse"
bakehouse.build_cost = {'clay': 2}
bakehouse.fees = {'food' : 1}
bakehouse.rank = 5
bakehouse.value = bakehouse.price = 8
bakehouse.type = "craftsman"
bakehouse.icon = "none"
bakehouse.owner = "blueprint"
bakehouse.usage_limit = 1
bakehouse.description = "Bake Bread with Grain. Spend 1 Energy and receive 1 Money for every 2 Bread baked."
get_quantity = requestblocks.GetQuantity('grain')
bakehouse.requests = [get_quantity]
give_grain = actionblocks.RemoveItems('grain', 1)
spend_energy = actionblocks.SpendEnergy(0.5)
get_bread = actionblocks.AddItems('bread',1)
get_money = actionblocks.AddItems('money',0.5)
bakehouse.actions = [give_grain, spend_energy, get_bread, get_money]
