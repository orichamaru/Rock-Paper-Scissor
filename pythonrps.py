import time
import sys
import random
print("     @@@@@     Python Project   Rock-Paper-Scissor    @@@@@@ \n")
print("   *****        Player V/s Computer     ******  \n")
print("   *****         Press '1' to start   *****  \n")
ch = int(input())
while(ch == 1):

    ch1 = 1
    while(ch1 == 1):
       print('''
                Press 'R' for Rock
                Press 'P' for Paper
                Press 'S' for Scissor
            ''')

       inp = input()
       if( inp == 'R' or inp == 'r' ):
          inp1 = 'Rock'
          ch1 = 0
       elif( inp == 'P' or inp == 'p' ):
          inp1 = 'Paper'
          ch1 = 0
       elif( inp == 'S' or inp == 's' ):
          inp1 = 'Scissor'
          ch1 = 0
       else:
          print('Wrong Input')
          ch1 = 1
    comp =random.randint(1,4)
    if(comp == 1):
        com = 'Rock'
    elif( comp == 2):
        com = 'Paper'
    elif( comp == 3):
        com = 'Scissor'
    time.sleep(1)
    print( str(inp1) + "  V/s  " + str(com) )
    time.sleep(1)
    if( (inp == 'R' or inp == 'r') and comp == 1 ):
      print('''
               @@@ It\'s a Tie @@@    ''')
    elif( (inp == 'R' or inp == 'r') and comp == 2 ):
      print('''
               $$$$ You Loose $$$$   ''')
    elif( (inp == 'R' or inp == 'r') and comp == 3 ):
      print('''
               @@@ You Win @@@  ''')
    elif( (inp == 'P' or inp == 'p') and comp == 1 ):
       print('''
                @@@ You Win @@@ ''')
    elif( (inp == 'P' or inp == 'p') and comp == 2 ):
       print('''
                @@@ It\'s a Tie @@@ ''')
    elif( (inp == 'P' or inp == 'p') and comp == 3):
       print('''
                $$$  You Loose  $$$ ''')
    elif( (inp == 'S' or inp == 's') and comp == 1):
       print('''
               $$$ You Loose  $$$ ''')
    elif( (inp == 'S' or inp == 's') and comp == 2):
      print('''
               @@@  You Win  @@@  ''')
    elif( (inp == 'S' or inp == 's') and comp == 3):
      print('''
               @@@  It\'s a Tie @@@  ''')
    print('''
           ####   Do You Want To Play Again ####
           ''')
    choice = 1
    while(choice == 1):
        print('''
                     Press '1' to restart
                     Press '0' to bye
              ''')
        num = int(input())
        if( num == 1):    
           choice = 0
           ch = 1
        elif( num == 0):
            ch = 0
            choice = 0
        else:
            print("Valid Choice")
            choice = 1
      
    
         
