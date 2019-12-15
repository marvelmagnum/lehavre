import random
import os
import gamefunctions
from gamestate import GameState
from logic import Logic
from player import Player
from buildings import Building
from ships import Ship

# Initial commands
commands = {1: 'money',
            2: 'fish',
            3: 'wood',
            4: 'clay',
            5: 'iron',
            6: 'grain',
            7: 'cattle',
            8: 'buy buildings / ships',
            9: 'sell buildings / ships'}


def init():
    """ Init game """
    os.system('cls')
    print("\n====================")
    print("Welcome to LE HAVRE!")
    print("====================")
    random.shuffle(game_state.bases)  # shuffle bases

    #print("Add Players")
    player_count = 2 #int(input("Enter total player count (1-5): "))
    ai_count = 1 #int(input("Enter AI player count: "))
    # for i in range(0, player_count - ai_count):
    #     pname = input("P" + str(i+1) + " name: ")
    game_state.players.append(Player.create_player("Marvel"))
    #for i in range(0, ai_count):
    game_state.players.append((Player.create_player("AI")))
    Building.setup_offers(game_state)
    Ship.setup_rounds(game_state)

def update_offers(turn, pid):
    """ Shows turn values, player, sets bases and updates offers """
    game_state.current_player = game_state.players[pid];
    print("Current Player: " + game_state.current_player.name)
    print("Turn " + str(turn) + ": " + str(game_state.bases[turn - 1]))
    game_state.offers[game_state.bases[turn - 1][0]] += 1
    game_state.offers[game_state.bases[turn - 1][1]] += 1
    if len(game_state.bases[turn - 1]) > 2:
        print("PAY INTEREST")

    print("OFFERS", end=": ")
    for key, value in game_state.offers.items():
        print("[ " + key.title() + ": " + str(value) + " ]", end="")
    print()


def show_inventory():
    """ Shows the player inventory """
    print("INVENTORY", end=": ")
    for key, value in game_state.current_player.inventory.items():
        if value > 0:
            print("[ " + key.title() + ": " + str(value) + " ]", end="")
    print()


# TODO: Handle additional actions like buy/sell
def assemble_commands():
    """ Assemble the available commands """
    print("COMMANDS")
    for key, value in commands.items():
        print(str(key) + ": " + value.title())
    com_count = 10
    for b in game_state.constructed:          # available usable buildings
        print(str(com_count) + ": ", end="")
        if b.owner == 'game':
            print("City's ", end="")
        else:
            print(b.owner.name + "'s ", end="")
        print(b.name.title(), end="")
        if b.current_user != 'none':
            print(" <Occupied by " + b.current_user.name + ">", end="")
        if 'wharf' in b.name:
            if b.modernized is False:
                print(" - [" + b.description + b.non_modern_desc + "] ")
            else:
                print(" - [" + b.description + b.modern_desc + "] ")
        else:
            print(" - [" + b.description + "] ")
        com_count += 1
    return com_count


def process_command(com, count):
    """ Process command inputs """
    if 1 <= com <= 7:       # resource offers
        if commands[com] in game_state.current_player.inventory:
            game_state.current_player.inventory[commands[com]] += game_state.offers[commands[com]]
        else:
            game_state.current_player.inventory[commands[com]] = game_state.offers[commands[com]]
        game_state.offers[commands[com]] = 0
        return True

    elif com == 8:  # buy additional action
        game_state.current_player.perform_buy(game_state)
        return False

    elif com == 9:  # sell additional action
        game_state.current_player.perform_sell(game_state)
        return False

    elif com < count:   # usable buildings
        building = game_state.constructed[com - 10]
        if building.usage_limit == 0:
            print(building.name.title() + " is not usable.")
            return False

        if building.current_user != 'none':
            print(building.name.title() + " is already occupied.")
            return False

        fees_paid = gamefunctions.get_entry_cost(game_state, building)     # collect entry fees
        if fees_paid or not building.fees:
            use = 0
            while use < building.usage_limit:  # building which allow more than 1 use
                if building.use(building.ask(game_state)):
                    print(building.name.title() + " was successfully used.")
                    gamefunctions.occupy_building(game_state, building)
                    use += 1
                    if use < game_state.constructed[com-10].usage_limit:
                        print("Use the " + game_state.constructed[com-10].name.title() + " again ? ")
                        print("1. Yes")
                        print("2. No")
                        ans = input("? ")
                        if int(ans) != 1:
                            break
                else:   # use of building failed
                    print(building.name.title() + " could not be used.")
                    successful = False
                    break
            if use == 0 and fees_paid:  # refund fees if building could not be used
                for item in fees_paid:
                    game_state.current_player.inventory[item[0]] += item[1]
            if use == 0:
                return False
            else:
                return True


def run_game():
    init()
    rounds = 1
    turns = 1
    pid = 0
    while True:
        update_offers(turns, pid)
        show_inventory()
        command_count = assemble_commands()
        proceed = False
        if game_state.current_player.type == 'human':
            command = input("? ")
            if command.lower() == "quit":
                break
            com = int(command)
            proceed = process_command(com, command_count)
        elif game_state.current_player.type == 'computer':
            proceed = logic.process_ai(game_state)
            print(game_state.current_player.name.upper() + " has finished its turn...")
            input()

        if proceed == True:
            if turns == 7:
                turns = 1
                print("Round " + str(rounds) + " ends.")
                gamefunctions.round_end(game_state)
            else:
                turns += 1

            if pid >= len(game_state.players) - 1:
                pid = 0
            else:
                pid += 1


game_state = GameState()
logic = Logic()
run_game()
