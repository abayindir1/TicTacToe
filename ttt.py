import itertools
game1 = [[1, 0, 0],
         [2, 1, 2],
         [0, 1, 1]]


def win(currentGame):

    # horizontal win
    for row in currentGame:
        result = all(element == row[0] and row[0] != 0 for element in row)
        if result:
            print(f"Player {row[0]} is the winner horizontally")

    # vertical win
    for column in range(len(currentGame)):
        list = []
        for row in currentGame:
            list.append(row[column])
        if all(element == list[0] and list[0] != 0 for element in list):
            print(f"Player {list[0]} is the winner vertically")

    # diagonal win
    # left to right
    diagonals = []
    for x in range(len(currentGame)):
        diagonals.append(currentGame[x][x])
    if all(element == diagonals[0] and diagonals[0] != 0 for element in diagonals):
        print(f"Player {diagonals[0]} is the winner diagonally (\\)")
    # right to left
    diagonals2 = []
    for col, row in enumerate(reversed(range(len(currentGame)))):
        diagonals2.append(currentGame[row][col])
    if all(element == diagonals2[0] and diagonals2[0] != 0 for element in diagonals2):
        print(f"Player {diagonals2[0]} is the winner diagonally (/)")


win(game1)

def gameBoard(board, player=0, row=0, column=0, display=False):
    try:
        if board[row][column] != 0:
            print("You can't play there, it is filled")
            return board, False
        print("   0  1  2")
        if not display:
            board[row][column] = player
        for count, row in enumerate(board):
            print(count, row)
        return board, True
    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2", e)
        return board, False


play = True
while play:
    board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    gameWon = False
    board, _ = gameBoard(board, display=True)
    playerChoice = itertools.cycle([1, 2])
    while not gameWon:
        currentPlayer = next(playerChoice)
        print(f"Current player: {currentPlayer}")
        win(board)
        played = False
        while not played:
            colChoice = int(input("What column do you want to play? (0, 1, 2):"))
            rowChoice = int(input("What row do you want to play? (0, 1, 2):"))
            game, played = gameBoard(board, currentPlayer, rowChoice, colChoice)
