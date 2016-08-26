# Noughts and crosses game using dictionaries
import sys
# Create a blank board
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', \
           'low-M': ' ', 'low-R': ' '}

# Create finished board for demo
completeBoard = {'top-L': 'top-L', 'top-M': 'top-M', 'top-R': 'top-R',
                 'mid-L': 'mid-L', 'mid-M': 'mid-M', 'mid-R': 'mid-R',
                 'low-L': 'low-L', 'low-M': 'low-M', 'low-R': 'low-R'}

# Tuple used for validation of user inputs
validation = ('q', 'top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R')

# Function to print board to screen
def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# Function to valide user inputs
def validate(userinput):
    while userinput not in validation:
        print('invalid entry, try again')
        userinput=input()
    if userinput == 'q':
        sys.exit()
    return(userinput)

# Game starts, X goes first then alternates with O
turn = 'X'
# There are 9 goes
for i in range(9):
    printboard(completeBoard)
    print('\r')
    print('Turn for ' + turn + '. Move on which space?\n(press q to quit)')
    move = input()
    # Call validation function and pass the user input via the move variable
    checkedmove = validate(move)
    # Validated user input is returned
    theBoard[checkedmove] = turn
    printboard(theBoard)
    print('\r')
    # Alternate to next turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
# At the end exit
else:
    sys.exit()
