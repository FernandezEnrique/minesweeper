
import random

CELL_BIT_MINE    =   0
CELL_BIT_FLAG    =   1
CELL_BIT_CLEAR   =  2

CELL_EMPTY          = 0
CELL_MINED          = 0b001
CELL_FLAGGED        = 0b010
CELL_MINED_FLAGGED  = 0b011
CELL_CLEARED        = 0b100

STATE_GOING = 0

STATE_LOST  = 1

STATE_WON = 2

BOARD  = None

mines = 0
state = 0

def check_mine(x):
    return (((x) >> CELL_BIT_MINE) & 1 )

def check_flag(x):
    return (((x) >> CELL_BIT_FLAG) & 1 )

def check_clear(x):
    return (((x) >> CELL_BIT_CLEAR) & 1 )

def check_empty(x):
    return ((x) == 0 )

def get_board():
    return BOARD


def gameInit(lvertical, lhorizontal, lmines):
    global mines, BOARD
    mines = lmines
    BOARD = [[CELL_EMPTY for _ in range(lhorizontal)] for _ in range(lvertical)]

    n = 0
    x = 0
    y = 0

    while ( n < mines ):
        x = random.randint(0, lvertical-1)
        y = random.randint(0, lhorizontal-1)

        if(check_mine(BOARD[x][y])):
            continue
        
        BOARD[x][y] = CELL_MINED

        n += 1

        
def gameGetState():
    return state


def count_neighbor_mines( x, y):
    count = 0
    rows = len(BOARD)
    cols = len(BOARD[0])

    
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy

        
        if 0 <= nx < rows and 0 <= ny < cols:
            if check_mine(BOARD[nx][ny]):
                count += 1

    return count

def check_win():
    rows = len(BOARD)
    cols = len(BOARD[0])

    for i in range(rows):
        for j in range(cols):
            cell = BOARD[i][j]
            if check_mine(cell) and not check_flag(cell):
                return False

            if not check_mine(cell) and not check_clear(cell):
                return False

    return True





def gameFlagCell(x,y):
    global state
    if(check_clear(BOARD[x][y])):
        return

    BOARD[x][y] ^= 1 << CELL_BIT_FLAG

    print(BOARD[x][y])

    if(check_win()):
        state = STATE_WON


def gameClearCell(x, y):
    global state
    if check_clear(BOARD[x][y]) or check_flag(BOARD[x][y]):
        return

    elif check_mine(BOARD[x][y]):
        state = STATE_LOST
        return
    else:
        BOARD[x][y] ^= 1 << CELL_BIT_CLEAR

        if count_neighbor_mines(x, y) == 0:

            rows = len(BOARD)
            cols = len(BOARD[0])

            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and \
                    not check_clear(BOARD[nx][ny] and not check_mine(BOARD[nx][ny])):
                        gameClearCell(nx, ny)

        if (check_win()):
            state = STATE_WON

def print_board():
    rows = len(BOARD)
    cols = len(BOARD[0])
    for i in range(rows):
        for j in range( cols):
            print(BOARD[i][j], end=" ")
        print()