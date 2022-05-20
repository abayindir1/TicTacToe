game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def gameBoard(board, player, row, column):
    if player != 0:
        print("   0  1  2")
        board[row][column] = player   
        for count, row in enumerate(board):
            print(count, row)
        return board 
    else:
        print("You cannot play")   

gameBoard(game, 1, 0 ,1)