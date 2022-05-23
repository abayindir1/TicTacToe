import itertools
game1 = [[1, 0, 2],
         [0, 2, 2],
         [2, 1, 1]]


def win(currentGame):
    # horizontal win
    for row in currentGame:
        result = all(element == row[0] for element in row)
        if result:
            print(f"Player {row[0]} is the winner horizontally")
    # vertical win
    for column in range(len(currentGame)):
        list = []
        for row in currentGame:
            list.append(row[column])
        if all(element == list[0] for element in list):
            print(f"Player {list[0]} is the winner vertically")

    # diagonal win
    # right to left
    diagonals = []
    for x in range(len(currentGame)):
        diagonals.append(currentGame[x][x])
    if all(element == diagonals[0] for element in diagonals):
        print(f"Player {diagonals[0]} is the winner diagonally (\\)")
    # left to right
    diagonals2 = []
    for col, row in enumerate(reversed(range(len(currentGame)))):
        diagonals2.append(currentGame[row][col])
    if all(element == diagonals2[0] for element in diagonals2):
        print(f"Player {diagonals2[0]} is the winner diagonally (/)")


def gameBoard(board, player=0, row=0, column=0, display=False):
    try:
        print("   0  1  2")
        if not display:
            board[row][column] = player
        for count, row in enumerate(board):
                print(count, row)
        return board
    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2", e)


play = True
# players = [1, 2]
while play:
    board1 =[[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    gameWon = False
    board1 = gameBoard(board1, display=True)
    playerChoice = itertools.cycle([1,2])
    while not gameWon:
        currentPlayer = next(playerChoice)
        print(f"Current player: {currentPlayer}")
        colChoice = int(input("What column do you want to play? (0, 1, 2):"))
        rowChoice = int(input("What row do you want to play? (0, 1, 2):"))

        gameBoard(board1, currentPlayer, rowChoice, colChoice)
