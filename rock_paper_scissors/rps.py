#!/usr/bin/python

import sys

options = [["rock"], ["paper"], ["scissors"]]

def rock_paper_scissors(n):
  # If n is equal to 0, return an empty list(array).  
  if n == 0:
        return [[]] 
  
  # if n is equal to 1, return options.
  if n == 1:
        return options
  
  # Set the output to an empty list (since it will automatically generate from the rock_paper_scissors list).  
  output = []
  
  # Set a list equal to rock_paper_scissors(n -1)
  listRPS = rock_paper_scissors(n - 1)
  
  # for loop a sublist in ListRPS.
  for subList in listRPS:
        for play in options:
              newPlay = subList + play
              output.append(newPlay)
  return output
  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')