### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.
 
 
################################## HARD CODED INFO ##################################
BOARD_ROW = 5
BOARD_COL = 5
 
ENEMY_COLOR = 'Black'
OWN_COLOR = 'White'
 
ORIGINAL_STATE = {
        ('e', '4'): ('King', 'Black'), ('d', '4'): ('Queen', 'Black'), 
        ('c', '4'): ('Bishop', 'Black'), ('b', '4'): ('Knight', 'Black'), 
        ('a', '4'): ('Rook', 'Black'), ('a', '3'): ('Pawn', 'Black'), 
        ('b', '3'): ('Pawn', 'Black'), ('c', '3'): ('Pawn', 'Black'), 
        ('d', '3'): ('Pawn', 'Black'), ('e', '3'): ('Pawn', 'Black'), 
        ('e', '0'): ('King', 'White'), ('d', '0'): ('Queen', 'White'), 
        ('c', '0'): ('Bishop', 'White'), ('b', '0'): ('Knight', 'White'), 
        ('a', '0'): ('Rook', 'White'), ('a', '1'): ('Pawn', 'White'), 
        ('b', '1'): ('Pawn', 'White'), ('c', '1'): ('Pawn', 'White'), 
        ('d', '1'): ('Pawn', 'White'), ('e', '1'): ('Pawn', 'White')
    }
 
NUMBER_TO_ALPHA = {
    0: 'a', 1: 'b', 2: 'c', 3:'d', 4:'e'
}
 
ALPHA_TO_NUMBER = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4
}

# 5x Pawn(1), 1x Bishop(3), 1x Knight(3), 1x Rook(5), 1x Queen(10), 1x King(100)
MAX_SCORE = 126
 
################################## PIECES ##################################
class Piece:
    def __init__(self, type):
        self.type = type
        if type == OWN_COLOR:
            self.score = 0
        else:
            self.score = -0
    
    """ Get possible moves """
    def getMoves(self, row, col, state):
        return []
 
    """ Get score for piece """
    def getScore(self):
        return self.score
 
    """
    Verify if the location is out of the board
    """
    @staticmethod
    def isInvalid(row, column):
        return row < 0 or row >= BOARD_ROW or column < 0 or column >= BOARD_COL
 
 
class Knight(Piece):
    KNIGHT_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
 
    def __init__(self, type):
        self.type = type
        if type == OWN_COLOR:
            self.score = 3
        else:
            self.score = -3
    
    """ Get possible moves """
    def getMoves(self, row, col, state):
        result = []
 
        for i in self.KNIGHT_MOVES:
            tempRow = row + i[0]
            tempCol = col + i[1]
            
            if Piece.isInvalid(tempRow, tempCol):
                continue
 
            if (tempRow, tempCol) in state and state[(tempRow, tempCol)][1] == self.type:
                continue
 
            result.append((tempRow, tempCol))  
            
        return result
        
class Rook(Piece):
    def __init__(self, type):
        self.type = type
        if type == OWN_COLOR:
            self.score = 5
        else:
            self.score = -5
    
    """ Get possible moves """
    def getMoves(self, row, col, state):
        result = []
        # Bottom
        for i in range(row - 1, -1, -1):
            if (i, col) in state:
                if state[(i, col)][1] != self.type:
                    result.append((i, col))
                break
            result.append((i, col))
 
        # Up
        for i in range(row + 1, BOARD_ROW):
            if (i, col) in state:
                if state[(i, col)][1] != self.type:
                    result.append((i, col))
                break
            result.append((i, col))        
            
        # Left
        for i in range(col - 1, -1, -1):
            if (row, i) in state:
                if state[(row, i)][1] != self.type:
                    result.append((row, i))
                break
            result.append((row, i))
        
        # Right
        for i in range(col + 1, BOARD_COL):
            if (row, i) in state:
                if state[(row, i)][1] != self.type:
                    result.append((row, i))
                break
            result.append((row, i))
        
        return result
 
class Bishop(Piece):
    def __init__(self, type):
        self.type = type
        if type == OWN_COLOR:
            self.score = 3
        else:
            self.score = -3
    
    """ Get possible moves """
    def getMoves(self, row, col, state):
        result = []
 
        # Top right
        for i in range(1, BOARD_ROW):
            tempRow = row + i
            tempCol = col + i
            
            if Piece.isInvalid(tempRow, tempCol):
                continue
 
            if (tempRow, tempCol) in state:
                if state[(tempRow, tempCol)][1] != self.type:
                    result.append((tempRow, tempCol))
                break
 
            result.append((tempRow, tempCol))  
 
        # Bottom right
        for i in range(1, BOARD_ROW):
            tempRow = row - i
            tempCol = col + i
            
            if Piece.isInvalid(tempRow, tempCol):
                continue
 
            if (tempRow, tempCol) in state:
                if state[(tempRow, tempCol)][1] != self.type:
                    result.append((tempRow, tempCol))
                break
 
            result.append((tempRow, tempCol))  
 
        # Bottom left
        for i in range(1, BOARD_ROW):
            tempRow = row - i
            tempCol = col - i
            
            if Piece.isInvalid(tempRow, tempCol):
                continue
 
            if (tempRow, tempCol) in state:
                if state[(tempRow, tempCol)][1] != self.type:
                    result.append((tempRow, tempCol))
                break
 
            result.append((tempRow, tempCol))  
            
        # Top left
        for i in range(1, BOARD_ROW):
            tempRow = row + i
            tempCol = col - i
            
            if Piece.isInvalid(tempRow, tempCol):
                continue
 
            if (tempRow, tempCol) in state:
                if state[(tempRow, tempCol)][1] != self.type:
                    result.append((tempRow, tempCol))
                break
 
            result.append((tempRow, tempCol))  
        
        return result
        
class Queen(Piece):
    def __init__(self, type):
        self.type = type
        if type == OWN_COLOR:
            self.score = 10
        else:
            self.score = -10
        self.bishop = Bishop(type)
        self.rook = Rook(type)
    
    """ Get possible moves """
    def getMoves(self, row, col, state):
        result = []
 
        result.extend(self.bishop.getMoves(row, col, state))
        result.extend(self.rook.getMoves(row, col, state))
 
        return result
        
class King(Piece):
    KING_MOVES = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
 
    def __init__(self, type):
        self.type = type
        if type == OWN_COLOR:
            self.score = 100
        else:
            self.score = -100
    
    """ Get possible moves """
    def getMoves(self, row, col, state):
        result = []
 
        for i in self.KING_MOVES:
            tempRow = row + i[0]
            tempCol = col + i[1]
            
            if Piece.isInvalid(tempRow, tempCol):
                continue
 
            if (tempRow, tempCol) in state and state[(tempRow, tempCol)][1] == self.type:
                continue
 
            result.append((tempRow, tempCol))  
            
        return result
        
class Pawn(Piece):
    def __init__(self, type):
        self.type = type
        if type == OWN_COLOR:
            self.score = 1
        else:
            self.score = -1
    
    """ Get possible moves """
    def getMoves(self, row, col, state):
        result = []
        if self.type == ENEMY_COLOR:
            # ENEMY -> Row decrease
            tempRow = row - 1
 
            # Check straight
            if not Piece.isInvalid(tempRow, col) and not (tempRow, col) in state:
                result.append((tempRow, col))
 
            # Check can attack left
            if not Piece.isInvalid(tempRow, col - 1) and \
                ((tempRow, col - 1) in state and state[(tempRow, col - 1)][1] != self.type):
                result.append((tempRow, col - 1))
 
            # Check can attack left
            if not Piece.isInvalid(tempRow, col + 1) and \
                ((tempRow, col + 1) in state and state[(tempRow, col + 1)][1] != self.type):
                result.append((tempRow, col + 1))
 
 
        else:
            # SELF -> Row increase
            tempRow = row + 1
 
            # Check straight
            if not Piece.isInvalid(tempRow, col) and not (tempRow, col) in state:
                result.append((tempRow, col))
 
            # Check can attack left
            if not Piece.isInvalid(tempRow, col - 1) and \
                ((tempRow, col - 1) in state and state[(tempRow, col - 1)][1] != self.type):
                result.append((tempRow, col - 1))
 
            # Check can attack left
            if not Piece.isInvalid(tempRow, col + 1) and \
                ((tempRow, col + 1) in state and state[(tempRow, col + 1)][1] != self.type):
                result.append((tempRow, col + 1))
 
        return result
 
 
################################## GAME ##################################
 
class Game:    
    piece_set = {
        ('King', ENEMY_COLOR): King(ENEMY_COLOR),
        ('Queen', ENEMY_COLOR): Queen(ENEMY_COLOR),
        ('Bishop', ENEMY_COLOR): Bishop(ENEMY_COLOR),
        ('Knight', ENEMY_COLOR): Knight(ENEMY_COLOR),
        ('Rook', ENEMY_COLOR): Rook(ENEMY_COLOR),
        ('Pawn', ENEMY_COLOR): Pawn(ENEMY_COLOR), 
        
        ('King', OWN_COLOR): King(OWN_COLOR),
        ('Queen', OWN_COLOR): Queen(OWN_COLOR),
        ('Bishop', OWN_COLOR): Bishop(OWN_COLOR),
        ('Knight', OWN_COLOR): Knight(OWN_COLOR),
        ('Rook', OWN_COLOR): Rook(OWN_COLOR),
        ('Pawn', OWN_COLOR): Pawn(OWN_COLOR)
    }
 
    """
    Check if state is terminal
    """
    @staticmethod
    def isTerminal(state):
        # pieces = set(state.values())
        
        # # Own king or enemy king is captured
        # if ("King", OWN_COLOR) not in pieces or ("King", ENEMY_COLOR) not in pieces:
        #     return True

        if not state.whiteKing or not state.blackKing:
            return True

        return False
 
class State:
    def __init__(self, state={}, whiteKing=None, blackKing=None):
        self.state = {}

        for key, value in state.items():
            cell = (int(key[1]), ALPHA_TO_NUMBER[key[0]])
            self.state[cell] = value
            if value == ('King', 'Black'):
                blackKing = cell
            elif value == ('King', 'White'):
                whiteKing = cell
        
        self.whiteKing = whiteKing
        self.blackKing = blackKing
 
    def copy(self):
        newState = State(whiteKing=self.whiteKing, blackKing=self.blackKing)
        newState.state = self.state.copy()
        return newState
 
    '''
    Calculate the score of the state base on the score allocated to each piece.
    '''
    def getScore(self):
        score = 0
 
        for piece in self.state.values():
            score += Game.piece_set[piece].getScore()
        
        return score
 
    '''
    Return all possible moves for the pieces
    '''
    def getNextMove(self, turn):
        result = {}
 
        for key, value in self.state.items():
            if value[1] == turn:
                result[key] = Game.piece_set[value].getMoves(key[0], key[1], self.state)

                # If any move will result in eating the king, return only that move
                if turn == OWN_COLOR and self.blackKing in result[key]:
                    return {key: [self.blackKing]}

                if turn == ENEMY_COLOR and self.whiteKing in result[key]:
                    return {key: [self.whiteKing]}
 
        return result
 
    '''
    Move piece from row1, col1 to row2, col2
    '''
    def makeMove(self, row1, col1, row2, col2):
        newState = self.copy()
 
        piece = newState.state.pop((row1, col1))
        newState.state[(row2, col2)] = piece

        if self.whiteKing == (row1, col1):
            newState.whiteKing = (row2, col2)

        elif self.blackKing == (row1, col1):
            newState.blackKing = (row2, col2)

        if self.whiteKing == (row2, col2):
            newState.whiteKing = None
        
        elif self.blackKing == (row2, col2):
            newState.blackKing = None
 
        return newState
 
#Implement your minimax with alpha-beta pruning algorithm here.
def ab(gameboard):
    MAX_DEPTH = 4
 
    # Helper function for the alpha-beta
    def helper(state, turn, alpha, beta, depth):
        if depth == MAX_DEPTH:
            return state.getScore(), None
 
        # check terminal state
        if Game.isTerminal(state):
            return state.getScore(), None
 
        if turn == OWN_COLOR:
            # Max-value (PLAYER)
            val =  -MAX_SCORE - 1
            bestMove = None
            allAvailMoves = state.getNextMove(OWN_COLOR)
 
            for (row, col), moves in allAvailMoves.items():
                for row2, col2 in moves:
                    newVal, _ = helper(state.makeMove(row, col, row2, col2), ENEMY_COLOR, alpha, beta, depth + 1)
                    if newVal > val:
                        val = newVal
                        bestMove = ((row, col), (row2, col2))
                        alpha = max(alpha, val)
                    if val >= beta:
                        return val, bestMove
            return val, bestMove
        else:
            # Min-value (ENEMY)
            val = MAX_SCORE + 1
            bestMove = None
            allAvailMoves = state.getNextMove(ENEMY_COLOR)
 
            for (row, col), moves in allAvailMoves.items():
                for row2, col2 in moves:
                    newVal, _ = helper(state.makeMove(row, col, row2, col2), OWN_COLOR, alpha, beta, depth + 1)
                    if newVal < val:
                        val = newVal
                        bestMove = ((row, col), (row2, col2))
                        beta = min(beta, val)
                    if val <= alpha:
                        return val, bestMove
            return val, bestMove
 
 
    state = State(gameboard)
    
    _, result = helper(state, OWN_COLOR, -MAX_SCORE - 1, MAX_SCORE + 1, 0)
 
    return (
        (NUMBER_TO_ALPHA[result[0][1]], result[0][0]),
        (NUMBER_TO_ALPHA[result[1][1]], result[1][0])
    )
 
 
### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)
 
# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))
 
def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
 
    move = ab(gameboard)
    return move #Format to be returned (('a', 0), ('b', 3))
 
# print(studentAgent(ORIGINAL_STATE))