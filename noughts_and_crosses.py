# Noughts and crosses game using dictionaries

# Create a blank board
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', \
           'low-M': ' ', 'low-R': ' '}

completeBoard = {'top-L': 'top-L', 'top-M': 'top-M', 'top-R': 'top-R', \
                 'mid-L': 'mid-L', 'mid-M': 'mid-M', 'mid-R': 'mid-R', \
                 'low-L': 'low-L', 'low-M': 'low-M', 'low-R': 'low-R'}

# Function to print board to screen
def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# Print a sample board with references
printboard(completeBoard)
print('\r')

# X goes first then alternates with O
turn = 'X'
# There are 9 goes
for i in range(9):
    printboard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printboard(theBoard)
