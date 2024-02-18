def draw_board(spots):
  #f string(en string man kan putte veriabler i)
  board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
  print(board)
#sjekker hvem sin tur det er
def check_turn(turn):
  if turn % 2 == 0: return 'O'
  else: 
    return 'X'

#sjekker om noen har fått tre på rad enten horisontalt, vertikalt eller diagonalt.
def check_for_winn(spots):
#Håndterer horisontale
  if   (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
    return True
#håndterer virtikale
  elif (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
    return True
#håndterer diagonal
  elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
    return True

  else: return False