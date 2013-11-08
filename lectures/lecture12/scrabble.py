import copy

#Get an array initialized, 15x15
def make_board():
    board = []
    for i in range(15):
        row = []
        for j in range(15):
            row.append({})
        board.append(row)
    return board

def play_letter(letter, board, position):
    """
    Takes the given letter and board, and checks if the position on the board
    can accept that letter.

    If so, modifies the board to have that letter on it.

    If not, raises an error.
    """
    row, column = position
    square = board[row][column]
    if 'letter' in square:
        if letter != square['letter']:
            raise Exception('You tried to play %s, but the board contained %s' %
                        (letter, square['letter']))
    else:
        square['letter'] = letter

def print_board(board):
    """
    Print a board so that each row is on its own line.
    An empty space is represented by '.'
    A played letter is represented by that letter
    """
    for row in board:
        for square in row:
            if 'letter' in square:
                print square['letter'],
            else:
                print '.',
        print

HORIZONTAL, VERTICAL = ("horizontal", "vertical")

def play_word(board, word, position, orientation):
    """
    board: Board to place the word on.  See above.

    word: the string word to play

    position: a tuple of coordinates (row, column) for the initial letter of the
    word to play.

    orientation: either "horizontal" or "vertical"

    raises an error if the coordinates for the word don't fall within the board.

    raises an error if the word conflicts with letters already on the board.

    returns a new board with the new word on it, as well as all the words
    already on the board.
    """
    #make the new board
    board = copy.deepcopy(board)
    #for every letter in the word to add
    #   find its coordinates
    #   check to see if it conflicts
    #   if the square is empty, play on it
    #   If the square is occupied, report any conflicts, but otherwise leave alone
    row, column = position
    for l in word:
        play_letter(l, board, (row, column))
        if orientation == HORIZONTAL:
            column += 1
        elif orientation == VERTICAL:
            row += 1
    return board
