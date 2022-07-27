from pip._vendor.rich.table import Column
def print_stats(direct_hits, missiles_fired, hits_required):
    """
    print_stats is used to format and print the game statistics
    
    :param direct hits: the number of direct hits achieved by the player
    :param missiles fired: the number of missiles fired by the player
    :param hits_required: a total number of 'ocean' spaces occupied by enemy ships
    :return: Nothing is returned. This function is designed to print to terminal 
    """
    
    print("\n") #formatting  (new lines)
    print(" _______________________________________") #print top border
    print("|                                       |") #print white space
    print("| Missiles fired:             %3s" % str(missiles_fired) + "       |") #display & format missiles fired
    print("| Direct hits:                %3s" % str(direct_hits) + "       |") #display & format hits
    print("| Targetting accuracy:        %4s" % str("{:.0%}".format(direct_hits/missiles_fired)) + "      |") #calculate and display accuracy as a 3 digit percentage
    print("| Enemy hit points remaining: %3s / %3s |" % (hits_required-direct_hits, hits_required)) #display remaing hit points over total hit points
    print("|_______________________________________|") #print white space
    print("\n") #formatting (new lines)
    
    return

def build_board (vertical_height, horizontal_length): 
    """
    Build_board is used to draw the board, and fill it with empty 'ocean' tiles (" O ") 
    based on game options horizontal_length and vertical_height. This is done as a list
    of lists. Each row will contain a list of strings (" O ") for each column.
    
    :param vertical_height: an integer defining the board height. Passed from a global variable or user input.
    :param horizontal_length: an integer defining the board width. Passed from a global variable or user input.
    :return: a list of lists called board is returned as described above.
    
    """
    empty_board = [] #initiate a temp variable list
    for i in range(vertical_height): #loop through required rows
        column = [] #create a column list
        for j in range(horizontal_length): #loop through required columns
            column.append(" O ") #create empty 'ocean' blocks
        empty_board.append(column) #add the row list as a new column on the board
    return empty_board #return the empty ocean board

def print_board(board, valid_rows_display, valid_columns_display):
    """
    Accepts an input 'board' which is expected to be a list of equal length lists defining the board. 
    Prints the board formatted for game play. This function is designed to print the board contents with 
    specific formatting and does not return anything.
    
    :param board: a list of lists mapping the board. Example: [" M ", " O ", " O "], [" O ", " X ", " O "]
    :return: None. Function is used to print to terminal.
    """
    
    index = 1 #used to count loops for creating and formatting new lines
    count = 0 #Used for indexing the valid_rows_display var
    border_bar = "" #used to store the length of the top and bottom bars
    column_labels = str() #used to store a string of the formatted column labels
    
    for i in range(len(valid_columns_display)): #format column labels for printing based on board length
        column_labels += (" " + str(valid_columns_display[i]) + "  ") #format a string to use for printing column labels
    for i in range(len(column_labels)-2): #format a string to use as a top and bottom border for the board
        border_bar += "_" #add underlines for the length of the column labels
    print("    %s" % column_labels) #print the column labels
    print("\n  " + "  ___" + border_bar) #create a top border
    
    for lst in board: #iterate through rows (lists)
        for item in lst: #iterate through columns (list items)
            if index == 1: #print row labels on the first line
                print("%2s |" % (str(valid_rows_display[count])), end = "")
                #print(str(valid_rows_display[count]) + " |", end = "") #print row label
            print(item, end = " ") #print the indexed var                
            if index % len(valid_columns_display) == 0: #format new lines at the end of board length (normal people call this width, too late)
                print(" | " + str(valid_rows_display[count]) + "\n") #label the row and begin new line
                count += 1 #increment count for use in labeling rows
                if count > len(valid_rows_display) : #reset count if above the size of board height
                    count = 0 #reset var                    
            index += 1 #increment var used for horizontal sizing
            if index > len(valid_columns_display): #reset var if above board width
                index = 1 #reset var
    print("  " + "  ___"  + border_bar) #print a bottom border
    print("    %s" % column_labels) #print the column labels
    
    return "" #no return. Function used for printing to console only. "" eliminate a 'None' value

def launch_missile(valid_rows_display, valid_columns_display, radar_allowed, enemy_ships):
    """
    launch_missile is used to gather user input for strike coordinates. Instructions are displayed and input
    is requested. The input is verified for validity and reformatted as variables usable programmatically.
    For better user experience input is taken as an alpha to represent rows, and a number starting at 1 
    (not index 0). This user friendly input is converted to usable programmatic input before return. The 
    row is converted from alpha to an index (starting at 0) and the column is reduced by 1 to account for
    the 0 index.
    
    :param valid_rows_display: a list of valid rows. List items are expected to be upper case alpha as expected by user.
    :param valid_columns_display: a list of valid columns. List items should start at int 1.
    :param radar_allowed: a string containing yes/no user input for using radar
    :param enemy_ships: used to import a board of ship locations for use in the radar_report function if used 
    :return: target_row and target_column formatted for use referencing list indexes (int >= 0)
      
    """
    coord_input = str() #initialize the user input variable with 0
    target_row = int() #define input variable for row
    target_column = int() #define input variable for column
    radar_usage = int()

    while target_row not in valid_rows_display or target_column not in valid_columns_display:
        print("*******************************************************")
        print("      TEST: Tactical Execution System Targetting    ") #print instructions
        print("\n  Provide strike coordinates.") #print instructions
        print("  Example: Launch at the 2nd row's 3rd column use B3.") #print instructions
        print("  Valid rows are:   ", end = " ") #print instructions
        for i in valid_rows_display: #format and print valid display rows
            print(i, end = " ") #format to print on the same line 
        print("\n  Valid columns are:", end = " ") #print instructions
        for i in valid_columns_display: #format and print valid display columns
            print(i, end = " ") #format to print on the same line
        print("\n*******************************************************")
        
        print("To retreat from battle in disgrace, forever being deemded a coward:")
        print("Enter your new name: loser\n")
        
        if radar_allowed.lower() == "y":
            print("To ask for an intel report from the radar officer:")
            print("Enter: radar")
            print("-------------------------------------------------------")
            coord_input = input("\nEnter target coordinates, or option (radar (hint) | loser (quit): ") # take user input
        
        else:
            print("-------------------------------------------------------")
            coord_input = input("\nEnter target coordinates, or option (loser (quit)): ") # take user input
            
        if coord_input.lower() == "loser":
            print("\nYou have brought shame down upon yourself, your name, your country, and your family.")
            print("Don't let it get to you. Have a great day!")
            raise SystemExit #abort I'm not worthy!
        
        elif coord_input.lower() == "radar":
            radar_usage = radar_report(radar_usage, enemy_ships)
        target_row = coord_input[0].upper() #set target_row to the uper case version of the 1st character in the string
        target_column = coord_input[1:len(coord_input)] #set the target_column to the remainder of the string allowing for 2+ digits
        
        if target_column.isnumeric() == False: #if the 2nd string character and beyond is not numeric 
            target_column = int(0) #set it to 0 to continue the while loop (0 is always out of bounds for the display columns)
        target_column = int(target_column) #convert the string parsed from user input to an integer after verifying that won't cause an exception
    
    print("\nMissile Guidance Confirmed: Target Row: %2s | Target_Column: %2s | Coordinates: %2s" % (target_row, target_column, (str(target_row) + str(target_column)))) #print target

    target_row = valid_rows_display.index(target_row) #convert user indexing from alpha to numeric index starting at 0 for use in main program
    target_column -= 1 #convert user indexing starting at 1 to system indexing starting at 0 for use in main program
    
    return target_row, target_column

def radar_report(radar_usage, enemy_ships):
    """
    Used to provide the player with hints. Hints are provided a single enemy ship location coordinate. 
    Number of available hints is set via a variable for easy modification.
    :param radar_usage: how many times has radar been used
    :param enemy_ships: used to import a board of ship locations to use for hints 
    :return: radar_usage for storage in parent object across iterations
    """
    
    from random import randint #used to select a random coordinate from the board parameter
    from string import ascii_uppercase
    
    max_radar_use = 5 #variable to define max hints
    dict_keys = list(enemy_ships.keys()) #creates a list of dictionary keys (ships) from enemy_ships
    key_select = randint(0, len(dict_keys)-1) #creates a random int for selecting a key from dict_keys
    key = dict_keys[key_select] #creates a variable called keys (selected randonly) to use in accessing the dictionary
    index_select = randint(0, len(enemy_ships[key])-1) #creates a random int for selecting an index from the key list
    coord_value = (enemy_ships[key][index_select]) #stores one randomly selected ship coordinate
    temp_coords = coord_value.split(":") #splits the coordinates into a two item list
    x = int(temp_coords[0]) #stores the raw (0 included) row index
    y = int(temp_coords[1]) + 1 #stores the user modified (0 excluded) column index
    x = ascii_uppercase[x] #modifies x to the user coordinate (alpha char) 
    hint = "%s:%s" % (x,y) #stores the hint to be provided to the user

    if radar_usage < max_radar_use:
        print("\n\n\n------------------------------------------------------------")
        print("Captain the radar officer is reporting activity at coordinates %s." % (hint))
        print("------------------------------------------------------------\n\n\n")
        radar_usage += 1
    else:
        print("\n\n\n-------------------------------------------------------------")
        print("Captain the radar officer is screaming something about giving it all they've got in a Scottish accent.")
        print("You're on your own.")
        print("------------------------------------------------------------\n\n\n")
    
    return radar_usage 