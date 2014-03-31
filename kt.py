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

# Creates an empty board
# param num_row is an integer
# param num_col is an integer
# returns an empty (all 0's) board num_row x num_col
def create_brd( num_row, num_col ):
  empty = 0
  brd = dict()
  i = 0
  j = 0
  while i <  int( num_row ):
    while j < int( num_row ):
      entry = i, j
      brd[ entry ] = empty
      j += 1
    i += 1
  return brd

# Finds where the knight is on the board
# param brd is a board
# returns knights current position in tuple
# RESTRICTION: does not work on blank board
def find_pos( brd ):
  beg_tup = [ (0,0) ]
  num = brd[ beg_tup ]
  for i in len( brd ):
    for j in len( brd ):
      new_tup = (0, i)
      new_num = brd[ new_tup ]
      if new_num > num:
        num = new_num
        beg_tup = new_tup
  return beg_tup
