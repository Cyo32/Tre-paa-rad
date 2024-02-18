import os
#importerer kode fra "Helpers.py". først spesiviserer jeg at de neste komandoene skal gis til "Helpers.py" og derreter sier vi hvilke funksjoner som skal imorteres
from Helpers import  check_turn, check_for_winn, draw_board

spots= {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5',6 : '6', 7 : '7',  8 : '8', 9 : '9'}
  
playing, complete = True, False
turn = 0
prev_turn = -1

while playing:
    #reset terminalen
      os.system('cls' if os.name == 'nt' else 'clear')
      draw_board(spots)
      print("Skriv et tall mellom 1 og 9, eller skriv q for å avslutte")
      #forteller spilleren at verdien allerede er endret
      if prev_turn == turn:
        print("Ugyldig valg!")
      prev_turn = turn
      print("Spiller " + str((turn % 2) + 1) + " sin tur")
    #input av spilleren (linje 19 til 26)
      choice = input()
      if choice == 'q':
          playing = False
    # sjekker om spilleren ga et nummer mellom 1 og 9 og om nummeret mellom 1 og 9 allerede er tatt
      elif str.isdigit(choice) and int(choice) in spots and not spots[int(choice)] in {"X", "O"}:
          turn += 1
          spots[int(choice)] = check_turn(turn)
  # sjekker om spillet har hatt 9 runder
      if turn == 9:
        playing = False
    #Sjekker om noen har vunnet
      if check_for_winn(spots): 
        playing, complete = False, True
      
    #Hvis det er en vinner, så forteller denne hvem som vant
      if complete:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)
        if check_turn(turn) == 'X':
          print("Spiller 1 vant!")
        else: 
          print("Spiller 2 vant!")
    #Hvis det er uavgjort
      else:
        print("Uavgjort :-)")
