#!/usr/bin/python
#
# KnightsTour.py
#
# Created by John Van Note
#
# This program will attempt to move a knight on a chess board
# so that each space is visited exactly once. It will accept the
# input from the user in the following order:
# rows (# of rows on board)
# columns (# of columns on board)
# attempts (# of attempts we have to do this)
#
# Created: 10/31/11 - Spooky, I know
#
# Tabspace: 2
#
# LEFT moves and moves UPWARD are POSITIVE (+)
# RIGHT moves and moves DOWNWARD are NEGATIVE (-)

import sys
import random

def main():
  # Makes sure the user input is the approriate number of variables
  if len( sys.argv ) != 4:
    print "ERROR! Number of arguments invalid, 3 arguments needed:"
    print "rows \ncolumns \nattempts"
  
  else:
    # Takes arguments from user, verifies their value
    KNIGHT_ROWS = int( sys.argv[1] )
    KNIGHT_COLS = int( sys.argv[2] )
    KNIGHT_ATTS = int( sys.argv[3] ) 
    assert( KNIGHT_ROWS > 0 )
    assert( KNIGHT_COLS > 0 )
    assert( KNIGHT_ATTS > 0 )     
    i = 1
    is_success = 0
    cont = 0

    while i <= KNIGHT_ATTS and is_success != 1:
      # Creates empty board
      board = create_brd( KNIGHT_ROWS, KNIGHT_COLS )
      # Special occasion for 1X1 boards
      if KNIGHT_ROWS == 1 and KNIGHT_COLS == 1:
        is_success = 1
      else:
        # Starting point
        row = 0
        column = 0
        move_count = 2
        tour = tour_brd( row, column, board, move_count, KNIGHT_ROWS,
KNIGHT_COLS)
        if tour == 0:
          pass
        elif tour == 1:
          print "SUCCESS:"
          is_success = 1
        else:
          print "DEBUG!"
        i = i + 1

    if is_success == 0:
      print "FAIL:"
    prnt_brd( board )

  return 0

# create_brd: Creates an empty board 
# @param x: an integer for number of rows
# @param y: an integer for number of columns
# @return: empty (all 0's) list of list except a 1 in the first position
def create_brd( x, y ):
  brd = list()
  for j in range( 0, int( x )):
    brd.append( [0] * y )
  brd[0][0] = 1
  return brd

# place: Places the knight on the row, column areas of the board
# ... also place the num equal to the move the knight is on
# @param x: an integer where the knight will go by row
# @param y: an integer where the knight will go by column
# @param brd: a list of list that is the current board
# @param mv: the number mv that the function is on
# @return: a new board with mv in the postion
def place( x, y, brd, mv ):
  brd[x][y] = mv
  return brd

# check_mvs: Looks for all valid moves that the knight can make
# @param x: an integer of the knights current row position
# @param y: an integer of the knights current col position
# @param brd: a list of list that is the current boardi
# @param max_x: the total rows
# @param max_y: the total columns
# @return: all valid moves for the knight
def check_mvs( x, y, brd, max_x, max_y ):
  val_mvs = []
  prev = []
  all_mvs = [[2,1],[1,2],[-2,1],[-1,2],[2,-1],[1,-2],[-2,-1],[-1,-2]]
  for mvs in all_mvs:
    tmp_x = x 
    tmp_y = y 
    tmp_x = tmp_x + mvs[0] 
    tmp_y = tmp_y + mvs[1] 
    is_val = validate( tmp_x, tmp_y, brd, max_x, max_y ) 
    if is_val == 1:
      val_mvs.append( [ tmp_x, tmp_y ] )
  return val_mvs

# validate: Checks whether or not a knights move is valid
# @param mv_att: the move that is going to be attempted
# @param brd: the current board the night is attempting
# @param max_x: the total rows
# @param max_y: the total columns
# @return: 1 if the move is valid. 0 otherwise
def validate( x, y, brd, max_x, max_y ):
  if x < 0:
    return 0
  elif y < 0:
    return 0
  elif x >= max_x:
    return 0
  elif y >= max_y:
    return 0
  elif brd[x][y] != 0:
    return 0
  else:
    return 1

# walk_brd: Randomly chooses a new place on the board to move to
# @param x: rows
# @param y: columns
# @param brd: a list of list that represents the board
# @param mv: an integer if the mv that the knight is at
# @param max_x: the total rows
# @param max_y: the total columns
# @return: updated board
def walk_brd( x, y, brd, mv, max_x, max_y ):
  val_mvs = check_mvs( x, y, brd, max_x, max_y )
  if val_mvs == []:
    return [-1000000, -1, -1]
  else:
    pick = random.choice( val_mvs ) 
    new_brd = place( pick[0], pick[1], brd, mv)
    x = pick[0]
    y = pick[1]
    return ( new_brd, x, y ) 

# tour_brd: Tours an entire board for one attempt, the function is recursive
# @param x: an integer for the row position of the knight
# @param y: an integer for the column position of knight
# @param brd: the current board the knight is one
# @param mv: the move that the knight is currently on
# @param brd_size: the overall board
# @return: 1 if the tour was successful, 0 if not
def tour_brd( x, y, brd, mv, max_x, max_y ):
  ans = walk_brd( x, y, brd, mv, max_x, max_y )
  new_brd = ans[0]
  x = ans[1]
  y = ans[2]
  brd_size = max_x * max_y
  if new_brd == -1000000:
    return 0
  elif mv == brd_size:
    return 1
  else:
    mv = mv + 1
    return tour_brd( x, y, new_brd, mv, max_x, max_y )  
  
# prnt_brd: Prints the state of the knights board with the num move on the space
# @param brd: a list of lists that represents the current knight board
# @param max_x: the total number of rows in a board
# no return
def prnt_brd( brd ):
  for i in brd:
    for j in i:
      if j == 0:
        j = 'x'
      print str( j ) + "\t",
    print "\n"
  return

# Makin' sure everything runs when it is supposed to
if __name__ == "__main__":
  main()
