import random
def board(tile):
    print(tile[7]+"|"+tile[8]+"|"+tile[9])
    print("-+-+-")
    print(tile[4]+"|"+tile[5]+"|"+tile[6])
    print("-+-+-")
    print(tile[1]+"|"+tile[2]+"|"+tile[3])
    
def display_rules():
    print("The player is \"X\" and the computer is \"O\"")

def check_win(positions):
##win = (1,2,3) or (4,5,6) or (7,8,9) or (7,4,1) or (8,5,2) or (9,6,3) or (7,5,3) or (9,5,1)
    return (((1 in positions) and (2 in positions) and (3 in positions)) or\
            ((4 in positions) and (5 in positions) and (6 in positions)) or\
            ((7 in positions) and (8 in positions) and (9 in positions)) or\
            ((7 in positions) and (4 in positions) and (1 in positions)) or\
            ((8 in positions) and (5 in positions) and (2 in positions)) or\
            ((9 in positions) and (6 in positions) and (3 in positions)) or\
            ((7 in positions) and (5 in positions) and (3 in positions)) or\
            ((9 in positions) and (5 in positions) and (1 in positions)))
            
             #e.g. False,False,True --> False
             #     True,True,True --> True                      

def game(tile):
    available = [1,2,3,4,5,6,7,8,9]
    player_positions = []
    computer_positions = []

    while True:
        try:
            print("="*30)
            print("Your turn")
            player_choice = int(input("Enter a position: "))
            if player_choice == 0 or player_choice in computer_positions or player_choice in player_positions:
                raise Exception
            tile[player_choice] = "X"
            player_positions.append(player_choice)
            available.pop(available.index(player_choice))

            #computer's turn
            computer_choice = random.choice(available)
            tile[computer_choice] = "O"
            computer_positions.append(computer_choice)
            available.pop(available.index(computer_choice))

            board(tile)
            
            print("\nPlayer(X):",player_positions)
            print("Computer(O):",computer_positions)
            #print("Available:",available)

            #check win
            if check_win(player_positions) == True:
                print("YOU WIN!")
                break
            if check_win(computer_positions) == True:
                print("COMPUTER WINS!")
                break
            if available == [] and check_win(player_positions) == False and check_win(computer_positions) == False:
                print("DRAW!")
                break
        except:
            print("\nINVALID INPUT. Choose from:",available,"\n")
            board(tile)
            print("\nPlayer(X):",player_positions)
            print("Computer(O):",computer_positions)
            if check_win(player_positions) == True:
                print("YOU WIN!")
                break
            if check_win(computer_positions) == True:
                print("COMPUTER WINS!")
                break
            if available == [] and check_win(player_positions) == False and check_win(computer_positions) == False:
                print("DRAW!")
                break

    prompt_replay = int(input("\nTo play again, enter [1]: \n"))
    if prompt_replay == 1:
        print("*"*30,"\n")
        main()
def main():
    tile = [None,"1","2","3","4","5","6","7","8","9"]
    board(tile)
    display_rules()
    game(tile)
    
main()
