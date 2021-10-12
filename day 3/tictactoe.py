global board
board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
player = "X"

def print_board(board):
    for line in board:
        print(line)

def make_move():
    global player
    x = int(input(f"Player {player}, What is the x coordinate? ").rstrip())
    y = int(input(f"What is the y coordinate? ").rstrip())

    while board[y][x] != " ":
        print('You must choose an empty spot')
        x = int(input(f"Player {player}, What is the x coordinate? ").rstrip())
        y = int(input(f"What is the y coordinate? ").rstrip())
    board[y][x] = player
    player = "O" if player == "X" else "X"

def isWin():
    #row
    global player
    if player == "O":
        p = "X"
    elif player == "X":
        p = "O"

    for x in range(3):
        win = True
        for y in range(3):
            if board[x][y] != p:
                win = False
                break
        if win:
            return True
    #column
    for x in range(3):
        win = True
        for y in range(3):
            if board[y][x] != p:
                win = False
                break
        if win:
            return True
    #diagonal
    win = True
    for x in range(3):
        if board[x][x] != p:
            win = False
    if win:
        return True

    win = True
    for x in range(3):
        if board[2-x][x] != p:
            win = False
    if win:
        return True

    return False

def tictactoe():
    print_board(board)
    make_move()

def main():
    gamewon = False
    while not gamewon:
        tictactoe()
        gamewon = isWin()
    print_board(board)
    if player == "O":
        p = "X"
    elif player == "X":
        p = "O"
    print(f"GAME OVER!! {p} won")
    

main()
