"""
A screen saver pattern generator
The screen is a grid
each cell is dead or alive
the state of a cell depends upon the state of it neighbors
"""
import os
import time


class screen_saver:

  def __init__(self, m, n):
    self.max_rows = m
    self.max_columns = n
    self.grid = [['dead'] * n for i in range(m)]
    self.grid[0][0]='alive'
    self.grid[m-1][n-1]='alive'
    self.grid[0][n-1]='alive'
    self.grid[m-1][0]='alive'
    #print('1. Idrees grid=', self.grid)
    #self.PrintGrid()

  def position(self, x, y):
    return (x % self.max_rows, y % self.max_columns)

  def ListOfNbrs(self, x, y):
    return (
      [self.position(x-1,y), 
      self.position(x+1, y), 
      self.position(x, y+1), 
      self.position(x, y-1),
      self.position(x-1, y-1), 
      self.position(x-1, y-1), 
      self.position(x+1,y+1), 
      self.position(x+1,y-1)
    ])

  def MoveToNextState(self, x, y):
    listOfNbrs = self.ListOfNbrs(x,y)
    alive_nbrs = 0
    for (nx,ny) in listOfNbrs:
      if 'alive' in self.grid[nx][ny]:
        alive_nbrs += 1
    
    if alive_nbrs < 2:
      return('dead')
    elif alive_nbrs == 2:
      return(self.grid[x][y])
    elif alive_nbrs == 3:
      return('alive')
    else:
      return('dead')


 
  def NextGrid(self):
    new_grid = self.grid
    for x in range(self.max_rows):
      for y in range(self.max_columns):
        new_grid[x][y] = self.MoveToNextState(x,y)
    self.grid = new_grid    

  def PrintGrid(self):
    for x in range(self.max_rows):
      print()
      for y in range(self.max_columns):
        #print('x,y=', x,y)
        if 'alive' in self.grid[x][y]:
          print('X', end='')
        else:
          print('-', end='')
    print()


def run():
  s = screen_saver(4, 4)
  #print('Nbrs=', s.ListOfNbrs(5,6))
  s.PrintGrid()
  while True:
    time.sleep(1)
    os.system('clear')
    s.NextGrid()
    s.PrintGrid()
  


