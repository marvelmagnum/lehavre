import random
import os
import gamefunctions
import gamestate

# Initial commands
commands = {1: 'money',
            2: 'fish',
            3: 'wood',
            4: 'clay',
            5: 'iron',
            6: 'grain',
            7: 'cattle'}


def init():
    """ Init game """
    os.system('cls')
    print("\n====================")
    print("Welcome to LE HAVRE!")
    print("====================")
    random.shuffle(gamestate.game_state.bases)  # shuffle bases


def update_offers(turn):
    """ Adds turn, sets bases and updates offers """
    print("Turn " + str(turn) + ": " + str(gamestate.game_state.bases[turn - 1]))
    gamestate.game_state.offers[gamestate.game_state.bases[turn - 1][0]] += 1
    gamestate.game_state.offers[gamestate.game_state.bases[turn - 1][1]] += 1
    if len(gamestate.game_state.bases[turn - 1]) > 2:
        print("PAY INTEREST")

    print("OFFERS", end=": ")
    for key, value in gamestate.game_state.offers.items():
        print("[ " + key.title() + ": " + str(value) + " ]", end="")
    print()


def show_inventory():
    """ Shows the player inventory """
    print("INVENTORY", end=": ")
    for key, value in gamestate.game_state.inventory.items():
        if value > 0:
            print("[ " + key.title() + ": " + str(value) + " ]", end="")
    print()


def assemble_commands():
    """ Assemble the available commands """
    print("COMMANDS")
    for key, value in commands.items():
        print(str(key) + ": " + value.title())
    com_count = 8
    for b in gamestate.game_state.constructed:          # available usable buildings
        print(str(com_count) + ": " + b.name.title(), end="")
        if b.current_user != 'none':
            print(" <Occupied by " + b.current_user.title() + ">", end="")
        print(" - [" + b.description + "] ")
        com_count += 1
    return com_count


def process_command(com, count):
    """ Process command inputs """
    if 1 <= com <= 7:       # resource offers
        if commands[com] in gamestate.game_state.inventory:
            gamestate.game_state.inventory[commands[com]] += gamestate.game_state.offers[commands[com]]
        else:
            gamestate.game_state.inventory[commands[com]] = gamestate.game_state.offers[commands[com]]
        gamestate.game_state.offers[commands[com]] = 0
    elif com < count:   # usable buildings
        if gamestate.game_state.constructed[com - 8].usage_limit == 0:
            print(gamestate.game_state.constructed[com - 8].name.title() + " is not usable.")
            return

        if gamestate.game_state.constructed[com - 8].current_user != 'none':
            print(gamestate.game_state.constructed[com - 8].name.title() + " is already occupied.")
            return

        fees_paid = gamefunctions.get_entry_cost(gamestate.game_state.constructed[com - 8])     # collect entry fees
        if fees_paid or not gamestate.game_state.constructed[com - 8].fees:
            use = 0
            while use < gamestate.game_state.constructed[com-8].usage_limit:  # building which allow more than 1 use
                if gamestate.game_state.constructed[com - 8].use(gamestate.game_state.constructed[com - 8].ask(gamestate.game_state)):
                    print(gamestate.game_state.constructed[com - 8].name.title() + " was successfully used.")
                    gamefunctions.occupy_building(gamestate.game_state.constructed[com - 8])
                    use += 1
                    if use < gamestate.game_state.constructed[com-8].usage_limit:
                        print("Use the " + gamestate.game_state.constructed[com-8].name.title() + " again ? ")
                        print("1. Yes")
                        print("2. No")
                        ans = input("? ")
                        if int(ans) != 1:
                            break
                else:   # use of building failed
                    print(gamestate.game_state.constructed[com - 8].name.title() + " could not be used.")
                    break
            if use == 0 and fees_paid:  # refund fees if building could not be used
                for item in fees_paid:
                    gamestate.game_state.inventory[item[0]] += item[1]



def run_game():
    init()
    rounds = 1
    turns = 1
    while True:
        update_offers(turns)
        show_inventory()
        command_count = assemble_commands()

        command = input("? ")
        if command.lower() == "quit":
            break
        com = int(command)
        process_command(com, command_count)

        if turns == 7:
            turns = 1
            print("Round " + str(rounds) + " ends.")
        else:
            turns += 1


run_game()
