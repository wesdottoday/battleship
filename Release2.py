#Module Import
from string import ascii_lowercase, ascii_uppercase
from battleship_functions import print_stats, build_board, launch_missile, print_board
from random import randint #used to create random ship placement

#Variable Declaration

#Game Options
vertical_height = 10 #sets board height. May get this from user input later
horizontal_length = 10 #sets board length. May get this from user input later
num_ships = 5 #number of ships to hide

#Global Variables
#alphabet = list(ascii_uppercase) #used to create row labels and verify row data
option = ["y","n","yes","no","Yes","No"] #valid selection options list
radar_allowed = str()
hidden_ships = [] # board map with hidden ships stored as strings using the ship number. ex: " 1 " Initiated using build_board
enemy_ships = {} #Global dictionary containing lists of ship coordinates with ship_name keys (ex: battleship)
hits_required = int(0) #incremented with the ship size when the ship is hidden using ship_hider. Used to win the game.
carrier = [] #list variable for carrier ships. Stores a list of the ships coordinates on the map as "x:y"
battleship = [] #list variable for carrier ships. Stores a list of the ships coordinates on the map as "x:y"
cruiser = [] #list variable for carrier ships. Stores a list of the ships coordinates on the map as "x:y"
submarine = [] #list variable for carrier ships. Stores a list of the ships coordinates on the map as "x:y"
destroyer = [] #list variable for carrier ships. Stores a list of the ships coordinates on the map as "x:y"
valid_rows_display = [] #initialize a list of valid row labels to store a set of valid upper case letter row labels 
#create the valid_rows_display list
for i in range(0, vertical_height): #use vertical_height var to iterate through max height
    valid_rows_display.append(ascii_uppercase[i]) #add an upper case letter label for each valid row
valid_rows_compute = [] # valid_rows_display is used for user display, while valid_rows_compute is used for computations
#create the valid_rows_compute list
for i in range(len(valid_rows_display)): #use the displayed row letters list to create a list of corresponding list indexes
    valid_rows_compute.append(int(i)) #add a sequential integer index for each valid row
valid_columns_display = [] #initialze a list of valid column labels for user display removing the 0 index for user experience
#create the valid_columns_display list
for i in range(1, horizontal_length + 1): #create a range of valid rows removing the 0 index
    valid_columns_display.append(int(i)) #add an number label for each valid column
valid_columns_compute = []
#create the valid_rows_compute list
for i in range(len(valid_columns_display)): #use the displayed column numbers list to create a list of valid corresponding list indexes
    valid_columns_compute.append(int(i)) #add a sequential integer index for each valid column

"""
def print_board(board):
    #prints the board variable (list of lists) formatted for game play
    index = 1 #used to count loops for creating and formatting new lines
    border_bar = "  __" #used to store the length of the top and bottom bars
    count = 0 #Used for indexing the alphabet var
    column_labels = "   " #used to label the columns
    
    for i in range(horizontal_length): #Create the border bar and column labels based on board width
        border_bar = border_bar + "____" #Append lines to border bar
        column_labels = column_labels + " " + str(1 + i) + "  " #Add number labels to column label var
    
    print(column_labels) #label the columns
    print(border_bar) #create a top border
    print("\n") #create a new line
    
    for i in board: #iterate through rows
        for j in i: #iterate through columns
            if index == 1: #print row labels on the first line
                print(alphabet[count] + " |", end = "") #print row label
            print(j, end = " ") #print the indexed var                
            if index % horizontal_length == 0: #format new lines at the end of board width
                print(" | " + alphabet[count] + "\n") #label the row and begin new line
                count += 1 #increment count for use in labeling rows
                if count > vertical_height: #reset count if above the size of board height
                    count = 0 #reset var                    
            index += 1 #increment var used for horizontal sizing
            if index > horizontal_length: #reset var if above board width
                index = 1 #reset var
    print(border_bar) #print a bottom border
    print(column_labels) #print the lower column labels
    return "\n"
"""

def check_ship_overlap(ship_name,enemy_ship_placement):
    #checks a list of ship coordinates against a dictionary of lists holding all hidden ships
    for coordinate in ship_name: #iterate through coordinates in the list
        for list in enemy_ship_placement: #iterate through the lists in the enemy_ship_placement dictionary
            for item in enemy_ship_placement[list]: #check each value in the first list against each value in dictionary list
                #print("If condition: " + str(coordinate==item) + " Coordinate: " + coordinate + " Item: " + item) #for testing only
                if coordinate == item: #checks the coordinate from the first for loop against the list items in this keys list
                    return True #returns a boolean for use in external logic checks
    else: 
        return False

def ship_hider(board, ship_name, ship_number, ship_length, enemy_ship_placement):
    #uses a ship name (ex: battelship), a ship number for identifying ships(Range: 1-num_ships), and a ship length (1-5) to hide a ship
    axis_select = bool(randint(1,2) % 2) #random true or false to use for determining ship position true = horizontal, false = vertical
    rand_row = randint(0, vertical_height-1) #random row selection for ship placement
    rand_col = randint(0, horizontal_length-1) #random column selection for ship placement
    ship_coord = [] #used to store an integer list of coordinates for the ship

    if axis_select == True: #tests for true and executes for horizontal positioning on success
        if rand_col+ship_length >= horizontal_length-1: #ensure ship fits on the board
            rand_col = (rand_col+ship_length) - (horizontal_length-1) #modify starting point for ship fit

        for i in range(ship_length): #build the ship
            index = i+rand_col #incremental index to build ship horizontally
            ship_name.append(str(rand_row) + ":" + str(index)) #adds the coordinates to a list named using ship_name parameter

        while check_ship_overlap(ship_name, enemy_ship_placement) == True: # call check_ship_overlap to prevent overlapping ships
            ship_name = [] #reset the ship_name var for new coordinates
            rand_col = randint(0, horizontal_length-1) #pick a new random start point
            if rand_col+ship_length >= horizontal_length-1: #ensure ship fits on the board
                rand_col = (rand_col+ship_length) - (horizontal_length-1) #modify starting point for ship fit            
            for i in range(ship_length): #build the ship
                index = int(i+rand_col) #create a variable to iterate the modified index
                ship_name.append(str(rand_row) + ":" + str(index)) #add the coordinates to the ship
        
    else:
        if rand_row+ship_length >= vertical_height-1: #ensure ship fits on the board
            rand_row = (rand_row+ship_length) - (vertical_height-1) #modify starting point for ship fit
        
        for i in range(ship_length): #build the ship
            index = i+rand_row #incremental index to build ship vertically
            ship_name.append(str(index) + ":" + str(rand_col)) #adds the coordinates to a list named using ship_name parameter

        while check_ship_overlap(ship_name, enemy_ship_placement) == True: #call check_ship_overlap to prevent overlapping ships
            ship_name = [] #reset the ship_name var for new coordinates
            rand_row = randint(0, vertical_height-1) #pick a new random start point
            if rand_row+ship_length >= vertical_height-1: #ensure ship fits on the board
                rand_row = (rand_row+ship_length) - (vertical_height-1) #modify starting point for ship fit 
            for i in range(ship_length): #build the ship
                index = int(i+rand_row) #create a variable to iterate the modified index
                ship_name.append(str(index) + ":" + str(rand_col)) #add the coordinates to the ship            
        
    for i in ship_name: #iterate through the string list
        ship_coord = i.split(":") #split the coordinates into a 2 item list
        x = int(ship_coord[0]) #modify to integer and store as x
        y = int(ship_coord[1]) #modify to integer and store as y
        board[x][y] = (" %s " % ship_number) #place the ship on the hidden_ships board 

    ship_hits = ship_length #add the new ships length to the total hits required
    return ship_name, ship_hits #return ship_name (now a list of coordinates) and ship_hits

def hide_ships(board):
    #hides ships on the hidden_ships board and stores them as a dictionary of lists with a ship_name key
    global carrier #access the global variable for modification
    global battleship #access the global variable for modification
    global cruiser #access the global variable for modification
    global submarine #access the global variable for modification
    global destroyer #access the global variable for modification
    enemy_ship_placement = {} #used to store a master list of hidden ships as list values in a dictionary with ship_name keys
    hits_required = 0 #used to store a sum of all ship lengths as a target hit count
    ship_number = 0 #intitializes the variable setting it to 0
    
    for i in range(0,num_ships): #iterate through creating a ship for the total number of ships set in the global var
        ship_number += 1
        if ship_number == 1: #create ship 1
            ship_name = carrier #assign the carrier list
            ship_length = 5 #assign ship length
            ship_name, ship_hits = ship_hider(board, ship_name, ship_number, ship_length, enemy_ship_placement) #call ship_hider
            hits_required += ship_hits #add ship length to the total hits required
            enemy_ship_placement["carrier"] = ship_name #adds the list of ship coordinates to the master dictionary using ship-name as key
        elif ship_number == 2: #create ship 2
            ship_name = battleship #assign the battleship list
            ship_length = 4 #assign ship length
            ship_name, ship_hits = ship_hider(board, ship_name, ship_number, ship_length, enemy_ship_placement) #call ship_hider
            hits_required += ship_hits #add ship length to the total hits required
            enemy_ship_placement["battleship"] = ship_name #adds the list of ship coordinates to the master dictionary using ship-name as key
        elif ship_number == 3: #create ship 3
            ship_name = cruiser #assign the cruiser list
            ship_length = 3 #assign ship length
            ship_name, ship_hits = ship_hider(board, ship_name, ship_number, ship_length, enemy_ship_placement) #call ship_hider
            hits_required += ship_hits #add ship length to the total hits required
            enemy_ship_placement["cruiser"] = ship_name #adds the list of ship coordinates to the master dictionary using ship-name as key
        elif ship_number == 4: #create ship 4
            ship_name = submarine #assign the submarine list
            ship_length = 3 #assign ship length
            ship_name, ship_hits = ship_hider(board, ship_name, ship_number, ship_length, enemy_ship_placement) #call ship_hider
            hits_required += ship_hits #add ship length to the total hits required
            enemy_ship_placement["submarine"] = ship_name #adds the list of ship coordinates to the master dictionary using ship-name as key
        elif ship_number == 5: #create ship 5
            ship_name = destroyer #assign the destroyer list
            ship_length = 2 #assign ship length
            ship_name, ship_hits = ship_hider(board, ship_name, ship_number, ship_length, enemy_ship_placement) #call ship_hider
            hits_required += ship_hits #add ship length to the total hits required
            enemy_ship_placement["destroyer"] = ship_name #adds the list of ship coordinates to the master dictionary using ship-name as key
        else:
            print("I have not thought this far through. Code WTF") #thinking through how to handle a user input number of ships and min/max numbers
    return board, hits_required, enemy_ship_placement #return the board with ships mapped to check hits against and total hits required
    
def play_again(radar_allowed): #Game opening
    play = str() # create play as a string var
    
    print("\nWelcome to Battleship!") #Opening message

    while play not in option: #verify user input using a list of supported answers
        play = input("Would you like to play a game? (Y/N): ") #prompt for input
        play = play.lower() #ensure user input is lowercase
    if play in "y" + "yes": #check for a yes
        while radar_allowed not in option: #verify user input using a list of supported answers
            radar_allowed = input("Would you like to have radar support? (Y/N): ") #prompt for input
            radar_allowed = radar_allowed.lower() #ensure user input is lowercase
        if radar_allowed in "y" + "yes": #check for a yes
            print("\nA wise leader uses all available information. Wise leaders are weak.\n") #begin the game
            play_game(radar_allowed) #begin the game
        elif radar_allowed in "n" + "no": #check for no
            print("\nI don't need no stinking intel!") #brave and smart are not often bedfellows
            print("Have a great game!\n") #Move to getting radar input
            play_game(radar_allowed) #begin the game
        else:
            print("Code WTF") #if we else my code is worse than I thought           
    elif play in "n" + "no": #check for no
        print("Well shucks...") #cry quietly
        raise SystemExit #abort!
    else:
        print("Code WTF") #if we else my code is worse than I thought
    return  

def play_game(radar_allowed):
    #build one board to show missile strikes, and one to hide enemy ships
    print("\n")
    p1_display_board = build_board(vertical_height, horizontal_length) #create a board to display for player 1
    p1_enemy_board = build_board(vertical_height, horizontal_length) #create a board to hide player 1's opponents ships
    p1_enemy_board, hits_required, enemy_ships = hide_ships(p1_enemy_board)# hide ships on the hidden board
    targets = [] #target verification list. Creates a str variable to represent each ship in play for use checking the hidden ship board.
    for i in range(num_ships): #create a list of strings used to store ship locations on a hidden board
        targets.append(" %s " % str(i+1)) #format the string for each ship
    missiles_fired = int(0) #initialize variable to count attempts
    direct_hits = int(0) #initialize an integer to track hits

    #print(print_board(p1_display_board)) #print the board to screen
    print(print_board(p1_display_board, valid_rows_display, valid_columns_display)) #print the board to screen
    print("\n") #formatting  (new lines)
    while direct_hits < hits_required: #prompt for user input until all ships destroyed
        target_row, target_column = launch_missile(valid_rows_display, valid_columns_display, radar_allowed, enemy_ships) #run launch missile module to accept target coordinates

        if p1_display_board[target_row][target_column] == " M ": #check to see if you've already missed there
            missiles_fired += 1 #increment the number of missiles fired
            targetting_accuracy = int(100 * direct_hits / missiles_fired) #calculate accuracy as a percent
            print("Sorry Captain, still no ship in that spot. No need to fire twice.") #insult the user
            print_stats(direct_hits, missiles_fired, hits_required)
            print(print_board(p1_display_board, valid_rows_display, valid_columns_display)) #print the board to screen            

        elif p1_display_board[target_row][target_column] == " X ": #check to see if you've already hit there
            missiles_fired += 1 #increment the number of missiles fired
            targetting_accuracy = int(100 * direct_hits / missiles_fired) #calculate accuracy as a percent
            print("Those coordinates are still a hit. You're nothing if not thorough.") #insult the user
            print_stats(direct_hits, missiles_fired, hits_required)
            print(print_board(p1_display_board, valid_rows_display, valid_columns_display)) #print the board to screen                    
            
        elif p1_enemy_board[target_row][target_column] in targets: #check for a hit
            missiles_fired += 1 #increment the number of missiles fired
            direct_hits += 1 #increment the number of mhits
            targetting_accuracy = int(100 * direct_hits / missiles_fired) #calculate accuracy as a percent
            print("Captain, that's a direct hit!") #stroke user ego
            print_stats(direct_hits, missiles_fired, hits_required)
            p1_display_board[target_row][target_column] = " X " #place an 'X' on the board to show the hit
            print(print_board(p1_display_board, valid_rows_display, valid_columns_display)) #print the board to screen

        else:
            missiles_fired += 1 #increment the number of missiles fired
            targetting_accuracy = int(100 * direct_hits / missiles_fired) #calculate accuracy as a percent
            print("Captain, that strike missed.") #notify the captain of poor targetting
            print_stats(direct_hits, missiles_fired, hits_required)
            p1_display_board[target_row][target_column] = " M " #place an 'M' on the board to show the hit
            print(print_board(p1_display_board, valid_rows_display, valid_columns_display)) #print the board to screen
    print("\n") #formatting  (new lines)
    print("Congratulations Captain! You've destroyed the enemy fleet!") #more user ego stroking
    play_again()
    return "" #play_game is operational and returns no values
    
play_again(radar_allowed) #Begin the game

