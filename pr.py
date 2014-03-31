#!/usr/bin/python

def main():
  x = 3
  y = cube( x )
  print x, y

def cube( x ):
  x = square( x ) * x
  return x

def square( x ):
  x = x * x
  return x

if __name__ == "__main__":
  main()
