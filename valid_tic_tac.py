"""
https://leetcode.com/problems/valid-tic-tac-toe-state/
"""
def validTicTacToe(board):
  """
  :type board: List[str]
  :rtype: bool
  """
  ret = False
  print('Board=', board)
  validTuples = ["XXX",""]
  if XstartsFirst(board):
    if OffByZeroOrOne(board):
      if OneWinner(board):
        ret = True
  print('Found valid board=', ret, "\n\n")
  
def Xcount(board, player):
  return board[0].count(player) + board[1].count(player) + board[2].count(player)

def XstartsFirst(board):
  ret = True
  count_X = Xcount(board, 'X')
  count_O = Xcount(board, 'O')
  if count_X == 0 and count_O == 1:
    ret = False
  print("Idrees X starts first:", ret, " or May be\n\n")
  return ret

def OffByZeroOrOne(board):
  ret = False
  count_X = Xcount(board, 'X')
  count_O = Xcount(board, 'O')

  if 0 <= count_X - count_O <= 1:
    ret = True
   
  print("Idrees OffByZeroOrOne :", ret, "; count_X=", count_X, " count_O=", count_O, "\n\n")
  return ret

def OneWinner(board):
  ret = False
  if (Winner(board, 'X') and Xcount(board, 'X') - Xcount(board, 'O') == 1) or (Winner(board, 'O') and Xcount(board, 'X') == Xcount(board, 'O')):
    ret = True
  return ret

def Winner(board, player):
  ret = False
  winning_patterns = [
    # Horizontal patterns
    board[0][0:3], board[1][0:3], board[2][0:3], 
    # Vertical patterns
    board[0][0]+board[1][0]+board[2][0], 
    board[0][1]+board[1][1]+board[2][1], 
    board[0][2]+board[1][2]+board[2][2], 
    # Diag patterns
    board[0][0]+board[1][1]+board[2][2], 
    board[0][2]+board[1][1]+board[2][0], 
    ]

  # print('Winning patterns=', winning_patterns)
  for pattern in winning_patterns:
    if pattern.count(player) == 3:
      # print('Found winning pattern=', pattern)
      ret = True
  print('Winner player=', player, ' ret=', ret)
  return ret