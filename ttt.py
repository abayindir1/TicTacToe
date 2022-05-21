game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

game1 = [[1, 1, 2],
        [1, 2, 2],
        [0, 2, 2]]

def horizontalWin(currentGame):
        for row in currentGame:
                result = all(element == row[0] for element in row)
                if result:
                        print(row)
                        print("You won!")
                else: 
                        print(row)

def verticalWin(currentGame):
        for column in range(len(currentGame)):
                list =[]
                for row in currentGame:
                        list.append(row[column])
                if all(element == list[0] for element in list):
                        print("You won!")

def diagonalWin(currentGame):


# def gameBoard(board, player, row, column, display=False):
#     try:
#         if player != 0 and not display:
#             print("   0  1  2")
#             board[row][column] = player
#             for count, row in enumerate(board):
#                 print(count, row)
#             return board
#         else:
#             print("You cannot play")
#     except IndexError as e:
#         print("Error: make sure you input row/column as 0 1 or 2", e)

diagonalWin(game1)
