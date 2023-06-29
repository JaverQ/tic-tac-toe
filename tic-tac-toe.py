board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
currentSymbol = "X"
winOptions = [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)],
              [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)],
              [(0, 2), (1, 2), (2, 2)], [(0, 0), (0, 1), (0, 2)],
              [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]


def draw_board():
    for j in range(0, 3):
        print(' |' + board[0][j] + '| ', ' |' + board[1][j] + '| ', ' |' + board[2][j] + '| ', end='\n' + '\n')


draw_board()


def game_is_over():
    for x in range(0, 3):
        for y in range(0, 3):
            if board[x][y] == " ":
                return False
    print("Draw!")
    return True


def check_winner(symbol):
    for i in winOptions:
        if board[i[0][0]][i[0][1]] + board[i[1][0]][i[1][1]] + board[i[2][0]][i[2][1]] == symbol + symbol + symbol:
            print(symbol, "is winner!")
            return True
    return False


while True:
    if checkWinner("X") or checkWinner("O") or gameIsOver():
        break
    x = int(input("Select horizontal coordinate: "))
    y = int(input("Select vertical coordinate: "))
    x -= 1
    y -= 1
    board[x][y] = currentSymbol
    if currentSymbol == "X":
        currentSymbol = "O"
    else:
        currentSymbol = "X"

    drawBoard()