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
    i = 0
    is_success = 0
    cont = 0

    while i < KNIGHT_ATTS or is_success != 1:
      # Creates empty board
      board = create_brd( KNIGHT_ROWS, KNIGHT_COLS )
      board_size = KNIGHT_ROWS * KNIGHT_COLS

      # Starting point
      row = 1
      column = 1
      move_count = 1

      while move_count <= board_size or cont != 1:
        board = walk_brd( row, column, board, move_count)
        if board == [-1,-1]:
          cont = 1
        if move_count == board_size:
          is_succss = 1
          cont = 1
        move_count += 1
      i += 1
    if is_success == 1:   
      print "SUCCESS"
      prnt_brd( board )
    elif i == KNIGHT_ATTS:
      print "FAILURE"
      prnt_brd( board )
    else:
      print "Please debug"
      exit()
  return 0

# Creates an empty board 
# param x is an integer for number of rows
# param y is an integer for number of columns
# returns and empty (all 0's) list of list excpet a 1 in the first position
def create_brd( x, y ):
  brd = list()
  for j in range( 0, int( y )):
    brd.append( [0] * x )
  brd[0][0] = 1
  return brd

# Places the knight on the row, column areas of the board
# ... also place the num equal to the move the knight is on
# param x is an integer where the knight will go by row
# param y is an integer where the knight will go by column
# param brd is a list of list that is the current board
# mv is the number mv that the function is on
# returns a new board with mv in the postion
def place( x, y, brd, mv ):
  brd[x][y] = mv
  return brd
  
# Looks for all valid moves that the knight can make
# param x is an integer of the knights current row position
# param y is an integer of the knights current col position
# param brd is a list of list that is the current board
# returns all valid moves for the knight
def check_mvs( x, y, brd ):
  b = 2
  s = 1
  val_mvs = []
  all_mvs = [ [b,s],[s,b],[-b,s],[-s,b],[b,-s],[s,-b],[-b,-s],[-s,-b] ]
  for mvs in all_mvs:
    tmp_x = x
    tmp_y = y
    tmp_x += mvs[0]
    tmp_y += mvs[1]
    if validate( tmp_x, tmp_y, brd ) == 1:
      val_mvs.append( [tmp_x,tmp_y] )
  return val_mvs

# Checks whether or not a knights move is valid
# mv_att is the move that is going tot be attempted
# brd is the current board the night is attempting  
def validate( x, y, brd ): 
  tot_col = len( brd ) - 1
  tot_row = 0
  for i in brd:
    tot_row += 1
  tot_row = tot_row - 1
  if tot_row < x:
    return 0
  elif tot_col < y:
    return 0
  elif 0 > x:
    return 0
  elif 0 > y:
    return 0
  elif brd[x][y] != 0:
    return 0
  else:
    return 1

# Randomly chooses a new place on the board to move to
# param x is rows
# param y is columns
# param brd is a list of list that represents the board
# param mv is an integer if the mv that the knight is at
# return updated board
def walk_brd( x, y, brd, mv ):
  val_mvs = check_mvs( x, y, brd )
  if val_mvs == []:
    return [-1,-1]
  else:
    pick = random.choice( val_mvs ) 
    new_brd = place( pick[0], pick[1], brd, mv)
    return new_brd
  
# Prints the state of the knights board with the num move on the space
# param brd is a list or list that represents the current knight board
# returns nothing
def prnt_brd( brd ):
  for x in brd:
    print x
  return

if __name__ == "__main__":
  main()
