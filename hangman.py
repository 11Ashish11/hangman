#welcome to hangman
#the names in the hangmam are of the indian cricket team

import random as rd
from time import sleep
def close():
    for i in range(5):
        print(f'\rprogram will be ended in {5-i} secs ',end="")
        sleep(1)
    print('\rprogram is ended:                                   ')
    exit()
from numpy.random import randint
import sys
print("""
welcome to my hangman 
you are given three attempts to play the game 
best of luck 
      """
)

name=input('enter your name\n')
chc=input(f'{name.upper()} press 1 if you want to continue and press any key to exit:  ')
if chc!='1':
    print(";-( sorry to se you go:    ")
    close()
words=['virat','sikhar','rohit','dhoni','rishab','bhuvi','bumrah','rahul','hardik','jadeja','chahal']
al='abcdefghijklmnopqrstuvwxyz'
while True:

 choosen_word=rd.choice(words)
 n,m=randint(0,len(choosen_word),2)
 if n==m:
    n=0
    m=len(choosen_word)-1
 guess_word=["-" for x in range(len(choosen_word))]
 guess_word[n]=choosen_word[n]
 guess_word[m]=choosen_word[m]
 print(guess_word)
 y=0
 while y<3:
  x=input('enter the  word:  ').lower()
  if x  in al:
  
   if x  in choosen_word:
        if x in guess_word:
            print("word is already guessed")
        for i in range(len(choosen_word)):
             if x==choosen_word[i]:
              guess_word[i]=x
              print(guess_word)
        
       
              
        if "-" not in guess_word:
            print(f'congrats {name.upper()} you did well and no  of wrong attemp={y}')
            break   
   else:
      y+=1
      print(f'wrong guess try again and attemp left {3-y}')
      
      continue
       
  else:
     y+=1
     print(f'invalid  input attemp left {3-y}')
     
     continue
 if y>=2:
      print(f'you loose the game and the word is {choosen_word.upper()}')    
 chc=input('wanna play again 1 for continue and press any key to exit:  ')
 if chc!='1':
     close()