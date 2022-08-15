# Gardner’s Mini-chess AI

## Background
In this game, the chess pieces are divided into two different colored sets, namely White and Black.
Each set consists of 10 pieces: one King, one Queen, one Rook, one Bishop, one Knight, and five
Pawns.

The game is played on a square board of 5 rows and 5 columns. The rows start from row 0 at the
top to row 4 at the bottom and the columns start from column ’a’ as the leftmost column to column
’e’ as the rightmost column. The White pieces are placed at rows 0 and 1 while the Black pieces
are placed at rows 3 and 4.

## Algorithm
The AI plays the game using alpha-beta pruning. To balance response and performance,
I used the algorithm up to a depth of 4. This algorithm plays the game as player WHITE. 

## Performance
This algorithm is tested in CS3243 Introduction to Artificial Intelligence. It is played against various intelligent agent and achieved a 100% rate
of either win or draw
