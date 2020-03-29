"""Programmed By : Ahmed Hodhod  (Egypt) """
##global variables
board = ['-','-','-','-','-','-','-','-','-']
game_square = 0
current = None
winning_collections = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),
                       (0,4,8),(2,4,6))


def draw_board():
    """Draw the game board """
    print(board[0],'|',board[1],'|',board[2])
    print(board[3],'|',board[4],'|',board[5])
    print(board[6],'|',board[7],'|',board[8])




def start_game():
    "Determine the current player"
    try:
        select_current_player = input('select who will start the game ( X or O ) . write x or o : ')
        if ord(select_current_player) in ( 79 , 88 ,120 ,111 ):
            global current 
            current = select_current_player.upper()
            print(current)
            draw_board()
        else:
            print('<<Plz , choose O or X only >>')
            start_game()
    except:
        print('make sure you have not entered spaces or multiple chars ')
        start_game()
        
    
##start the game 
start_game()





def check_winner(current):
    "Check if there is a winner after each play"
    for x in winning_collections:
        x = list(x)
        if board[x[0]] == board[x[1]] == board[x[2]] != '-' :
            if board[x[0]] == board[x[1]] == board[x[2]]  == current :
                print('{0} Wins , Congrats'.format(current))
                return True
            else :
                return False
            


            
def flip_player():
    "Flip player after each game"
    global current 
    if current == 'O':
        current = 'X'
    else :
        current = 'O'
           

while game_square  <= 9 :
    player_input = input( 'insert a number < 9 : ' )
    if player_input.isdigit():
        player_number = int(player_input)
        if player_number in range(1 , 10):
            
            if board[player_number-1] == 'O' or board[player_number-1] == 'X':
                continue
      
            game_square = player_number
            ##execute the play
            board[player_number-1] = current
            draw_board()
            ##check if there is a winner
            winner = check_winner(current)
            if winner :
                break
            else :
                flip_player()

            ##check if there is a tie 
            i = 0
            for x in board:
                if x != '-':
                     i = i + 1

            if i == 9 :
                print("Tie (cat's game)")
                break 
                        
        else :
                print('Warning Message<<Plz , enter number from 1 to 9 >>')
                continue
    else :
        print('Warning Message<<Plz , enter number from 1 to 9 >>')
        continue
        

##flip
##check winner
##check if  there is a tie
##check invalid input





