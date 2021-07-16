board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
game_is_running = True
winner = None


def play_game():

    # global winner
    print("Welcome to the Tic-Tac-Toe world!")
    display_board()

    while game_is_running:

        flip_turn(current_player)

        win_or_tie()

        flip_player()

    # if winner == None:
    #     print("T")
    
    if winner == "X" or winner == "0":
        print(winner  + " won!")
    elif winner == None:
        print("tie..")


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")





def flip_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

           
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Please choose a position from 1-9: ")

        position = int(position) - 1

            
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    display_board()


def win_or_tie():
    
    win_the_match()
    tie_the_match()

def win_the_match():

    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagnoal_winner = check_diagnoals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagnoal_winner:
        winner = diagnoal_winner
    else:
        winner = None


def check_rows():
    global game_is_running

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_is_running = False

    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    else:
        return None
   
     
def check_columns():
    global game_is_running

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_is_running = False

    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    else:
        return None

def check_diagnoals():
    global game_is_running

    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    

    if diag1 or diag2:
        game_is_running = False

    if diag1:
        return board[0]
    if diag2:
        return board[2]
    else:
        return None

def tie_the_match():
    global game_is_running

    if "-" not in board:
        game_is_running = False
        return True
    else:
        return False

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"



play_game()
