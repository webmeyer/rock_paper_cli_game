import random


# Main settings
WEAPONS = {'1': "ROCK", '2': "PAPER", '3': "SCISSORS", '4': "SAW"}  # Hold the WEAPONS
PLAYERS = []  # Hold the player's names
GAMES = [[0, 0, 0], [0, 0, 0]]  # Keep record of the player's GAMES win, lost and ties
ROUNDS = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Keep record od all the ROUNDS of the PLAYERS


# Function to display the show_menu
def show_menu():
    print("\n-- MENU -- \nPlease enter the number corresponding to your selection:\n" + "1 - Play Game\n2 - Show game rules\n3 - Show statistics\n4 - Exit\n")
    # While loop is break when the user inputs a right option, if not shows an error message and continue the loop
    while True:
        try:
            userInput = input()
            if int(userInput) in range(1, 5) and userInput != '':
                return userInput
            else:
                print("Wrong input! Please try again.")
                continue
        except ValueError:
            print("Please enter the number!")
            continue


# Collect the player's names
def get_player_names(PLAYERS):
    while True:
        try:
            # Ask the user to input a name
            PLAYERS.append(input("\n-- CHOOSE PLAYER NAMES --\nPlease enter the name for the FIRST player: "))
            # Checks if the input is between 5 and 20 characters length
            if len(PLAYERS[0]) > 4 and len(PLAYERS[0]) < 21:
                break
            else:
                # If there is a wrong input the program keeps asking the user to enter a player name
                print("\nWrong input, names must be more than 5 and less than 20 characters")
                PLAYERS.clear()
                continue
        except KeyboardInterrupt:
            print('Please try again!')
            continue


    while True:
        try:
            # Ask the user to input a second name
            PLAYERS.append(input("\nPlease enter the name for the SECOND player: "))
            if len(PLAYERS[1]) > 4 and len(PLAYERS[1]) < 21 and PLAYERS[0] != PLAYERS[1]:
                return PLAYERS
            else:
                # If there is a wrong input the program keeps asking the user to enter a player name different from the first one
                print("\nThe second name must be different from the first one!" if PLAYERS[0] == PLAYERS[
                    1] else "\nWrong input, names must be more than 5 and less than 20 characters")
                PLAYERS.pop(1)
                continue
        except KeyboardInterrupt:
            print('Please try again!')
            continue


# Select weapons for player
def select_weapon(player):
    print("\n-- SELECT WEAPON --\nPlease enter the number of the weapon for " + player + ": " +
          "\n1 - Rock\n2 - Paper\n3 - Scissors\n4 - Saw\n")

    while True:
        try:
            userInput = input()
            if int(userInput) in range(1, 5) and userInput != '':
                return userInput
            else:
                # If the user enter an option different from the existing ones, the program ask again
                print("\nWrong input! Please try again.")
                continue
        except ValueError:
            print("Please enter the number!")
            continue


# function to start the game
def start_game(PLAYERS, GAMES, WEAPONS, ROUNDS):
    # Collects the PLAYERS name
    PLAYERS = get_player_names(PLAYERS)
    weapon = []  # individual weapon store

    # 3 ROUNDS and accumulate the results
    for x in range(0, 3):
        weapon.append(select_weapon(PLAYERS[0]))  # Calls and collect the result of select weapon
        check_winners(PLAYERS[0], WEAPONS, weapon[0], ROUNDS[0],
                     ROUNDS[2])  # Compare the picked weapon against the computer generated one

        weapon.append(select_weapon(PLAYERS[1]))  # Calls and collect the result of select weapon for the second player
        check_winners(PLAYERS[1], WEAPONS, weapon[1], ROUNDS[1],
                     ROUNDS[3])  # Compare the picked weapon of the second player against the computer generated one
        weapon.clear()  # the results are collected on the main counters, the local one is cleared to keep playing

    # Print the round results and declare round win, loss or tie
    print("\n#####################################  GAME RESULT  #########################################")
    get_game_result(PLAYERS[0], GAMES[0], ROUNDS[0])
    get_game_result(PLAYERS[1], GAMES[1], ROUNDS[1])
    print("\n#############################################################################################")
    # clears the main one time counter but keeps the overall records
    for x in range(0, 2):
        for y in range(0, 3):
            ROUNDS[x][y] = 0


# Compare the WEAPONS of the PLAYERS and the computer randomly generated to define a round winner
# and returns the modifications to the data structures that hold the numbers
def check_winners(player, WEAPONS, weapon, round, totalROUNDS):
    pcPlay = str(random.randint(1, 4))  # computer generated own weapon from numbers [1,2,3]

    if weapon == pcPlay:
        # If the player and the computer are the same they are tied
        print("\n----------------------------   ROUND RESULT   ----------------------------------")
        print(player + " selected " + WEAPONS[weapon] + " and computer selected " + WEAPONS[pcPlay])
        print(">> Tied round!")
        print("--------------------------------------------------------------------------------")
        round[2] += 1
        totalROUNDS[2] += 1
        weapon = 0

    if weapon == '1':
        # If the player selects rocks evaluate the computer weapon
        print("\n----------------------------   ROUND RESULT   ----------------------------------")
        print(player + " selected " + WEAPONS[weapon] + " and computer selected " + WEAPONS[pcPlay])
        if pcPlay == '3' or pcPlay == '4':
            round[0] += 1
            totalROUNDS[0] += 1
            # If the computer picks scissors or saw the player wins
            print(">> " + player + " wins this round!")
            print("--------------------------------------------------------------------------------")
        else:
            round[1] += 1
            totalROUNDS[1] += 1
            # If the computer picks paper the computer wins
            print(">> Computer wins this round!")
            print("--------------------------------------------------------------------------------")
    elif weapon == '2':
        # If the player selected paper evaluate the computer weapon
        print("\n----------------------------   ROUND RESULT   ----------------------------------")
        print(player + " selected " + WEAPONS[weapon] + " and computer selected " + WEAPONS[pcPlay])
        if pcPlay == '1':
            round[0] += 1
            totalROUNDS[0] += 1
            # If the computer picks rock the player wins
            print(">> " + player + " wins this round!")
            print("--------------------------------------------------------------------------------")
        else:
            round[1] += 1
            totalROUNDS[1] += 1
            # In any other case the computer wins
            print(">> Computer wins this round!")
            print("--------------------------------------------------------------------------------")
    elif weapon == '3':
        print("\n----------------------------   ROUND RESULT   ----------------------------------")
        # If the player selects scissors evaluate the computer weapon
        if pcPlay == '2':
            round[0] += 1
            totalROUNDS[0] += 1
            # If the computer picks paper the player wins
            print("\n>> " + player + " wins this round!")
            print("--------------------------------------------------------------------------------")
        else:
            round[1] += 1
            totalROUNDS[1] += 1
            # In any other case the computer wins
            print("\n>> Computer wins this round!")
            print("--------------------------------------------------------------------------------")
    elif weapon == '4':
        print("\n----------------------------   ROUND RESULT   ----------------------------------")
        # If the player selects saw evaluate the computer weapon
        if pcPlay == '2' or pcPlay == '3':
            round[0] += 1
            totalROUNDS[0] += 1
            # if the computer selects paper or scissors the player wins
            print("\n>> " + player + " wins this round!")
            print("--------------------------------------------------------------------------------")
        else:
            round[1] += 1
            totalROUNDS[1] += 1
            # In any other case the computer wins
            print("\n>> Computer wins this round!")
            print("--------------------------------------------------------------------------------")


# Pick the overall winner
def get_match_result(GAMES):
    # If the PLAYERS have the same numbers of wins, losses and ties declare an overall tie
    if GAMES[0][0] == 0 and GAMES[1][0] == 0 and GAMES[0][1] == 0 and GAMES[1][1] == 0 and GAMES[0][2] == 0 and \
            GAMES[1][2] == 0:
        return "\t\t\t\t\t\t\tThere are no plays yet to declare a winner"
    elif GAMES[0][0] == GAMES[1][0]:  # If both PLAYERS have the same number of wins evaluate the losses
        if GAMES[0][1] == GAMES[1][1]:  # If both PLAYERS have the same number of losses evaluate the ties
            if GAMES[0][2] == GAMES[1][2]:  # If both PLAYERS have the same number of ties delare the tie
                return ("\t\t\t\t\t\t\t" + PLAYERS[0] + " and " + PLAYERS[1] + " are tied!")
            elif GAMES[0][2] > GAMES[1][2]:
                # If the player has more ties than the second player losses and wins are the same
                return ("\t\t\t\t\t\t\t" + PLAYERS[0] + " wins the match")
            else:
                # or the second player wins
                return ("\t\t\t\t\t\t\t" + PLAYERS[1] + " wins the match")
        elif GAMES[0][1] < GAMES[1][1]:
            # If the 1st player has less losses than the 2nd player the 1st wins
            return ("\t\t\t\t\t\t\t" + PLAYERS[0] + " wins the match")
        else:
            # or the 2nd player wins
            return ("\t\t\t\t\t\t\t" + PLAYERS[1] + " wins the match")

    elif GAMES[0][0] > GAMES[1][0]:
        # If the number of wins are higher that the 2nd player the 1st wins
        return ("\t\t\t\t\t\t\t" + PLAYERS[0] + " wins the match")
    else:
        # or the 2nd player wins
        return ("\t\t\t\t\t\t\t" + PLAYERS[1] + " wins the match")


# Select the game winner against the computer
def get_game_result(player, game, ROUNDS):
    if ROUNDS[0] >= 2:
        # If the player had win more than 2 round wins
        print("\n" + player + " WINS the game against the computer!")
        game[0] += 1
    elif ROUNDS[1] >= 2:
        # If the player has lost 2 or more round losses
        print("\n" + player + " LOST the game against the computer!")
        game[1] += 1
    elif ROUNDS[0] == 1 and ROUNDS[1] == 1 and ROUNDS[2] == 1:
        # If the win, loss and tie are 1 each the player tied the computer
        print("\n" + player + " TIED the game against the computer!")
        game[2] += 1
    elif ROUNDS[0] == 1 and ROUNDS[1] == 2 and ROUNDS[2] == 0:
        # Explicit if the player lost 2 round even if won 1 losses
        print("\n" + player + " LOST the game against the computer!")
        game[1] += 1
    elif ROUNDS[0] == 0 and ROUNDS[1] == 0 and ROUNDS[2] == 3:
        # 3 tied round the player tied the computer
        print("\n" + player + " TIED the game against the computer!")
        game[2] += 1
    elif ROUNDS[0] == 0 and ROUNDS[1] == 1 and ROUNDS[2] == 2:
        # 1 loss and 2 ties player losses
        print("\n" + player + " LOST the game against the computer!")
        game[1] += 1
    elif ROUNDS[0] == 1 and ROUNDS[1] == 0 and ROUNDS[2] == 2:
        # if the player won 1 round and tied 2 the player wins
        print("\n" + player + " WINS the game against the computer!")
        game[0] += 1


# Game rules
def show_game_rules():
    print("\n#############################     GAME RULES     ###################################################\n")
    print(
        "Winner of the round will be determined as follows:\na. Rock breaks scissors and Saw therefore rock wins over scissors and saw. Rock loses against paper.\n" +
        "b. Scissors cut paper therefore scissors win over paper. Scissors lose against rock and Saw.\n" +
        "c. Paper covers rock therefore paper wins over rock. Paper loses against scissors and saw.\n" +
        "d. Saw cuts through scissors and paper therefore saw wins over scissors and paper. Saw loses against rock.\n" +
        "e. If player and computer make the same selection, there is a tie.\n\n" +
        " -  Winner of the game against the computer is one who won more rounds (must account for ties)\n" +
        " -  Overall human winner is based on the greater number of won games against the computer and least\n" +
        "    games lost (must account for tie between human players)\n\n")
    print("\n####################################################################################################")


# Display the statistics
def show_stats(PLAYERS, GAMES, ROUNDS):
    # Padding the player's names for formating purposes
    try:
        pla1 = "{:<20}".format(PLAYERS[0])
        pla2 = "{:<20}".format(PLAYERS[1])

        print("#################################         STATISTICS         ########################################\n")
        print("Statistics for rocks, paper and scissors game\n\n")
        print("PLAYERS\t\tROUNDS:\t win\tLost\tTied\t\tGAMES:\t win\tLost\tTied")
        print(
            pla1 + "\t  " + str(ROUNDS[2][0]) + "\t   " + str(ROUNDS[2][1]) + "\t " + str(ROUNDS[2][2]) + "\t\t\t  " + str(
                GAMES[0][0]) + "\t " + str(GAMES[0][1]) + "\t " + str(GAMES[0][2]))
        print(
            pla2 + "\t  " + str(ROUNDS[3][0]) + "\t   " + str(ROUNDS[3][1]) + "\t " + str(ROUNDS[3][2]) + "\t\t\t  " + str(
                GAMES[1][0]) + "\t " + str(GAMES[1][1]) + "\t " + str(GAMES[1][2]) + "\n")

        # Call the oick overall winner function and print the return
        print(get_match_result(GAMES))

        print("\n####################################################################################################")
    except IndexError:
        print("You don't have any matches! Please start new game!")


# Main function
def main(WEAPONS, PLAYERS, GAMES, ROUNDS):
    print("\n##########################################################")
    print(">> Welcome to the game 'Rock, Paper, Scissors and Saw' <<")
    print("##########################################################")

    while True:
        # Show menu and returns the users selection
        option = show_menu()
        if option == '1':
            # game starts
            start_game(PLAYERS, GAMES, WEAPONS, ROUNDS)
            continue
        elif option == '2':
            # show the game rules
            show_game_rules()
            continue
        elif option == '3':
            # show the game statistics
            show_stats(PLAYERS, GAMES, ROUNDS)
            continue
        elif option == '4':
            # Exit
            print("\nGoodbye!\n")
            break


# Main call
if __name__ == '__main__':
    main(WEAPONS, PLAYERS, GAMES, ROUNDS)