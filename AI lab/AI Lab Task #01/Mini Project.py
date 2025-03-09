import Words as word
import Hangman_Stages as levels
import random

def GetWord(Random_Catogary):
    return random.choice(word.Words[Random_Catogary])
def PlayGame():
   Current_Word=GetWord(Random_Catogary)
   WordList=list(Current_Word) 
   print("Welcome To HangMan Game")
   print(Current_Word) 
   print(f"Hint! It is a {Random_Catogary} and it has {len(WordList)} letters")
   TotalAttempts=len(levels.hangman_stages)
   win_Cheak=0
   while TotalAttempts>0:
    Current_Turn=input("Enter Character: ")
    if Current_Turn in WordList:
        print("Correct")
        win_Cheak+=1
        if win_Cheak==len(WordList):
           print("You Win")
           return
    else:
        print("Wrong")
        print(f"{TotalAttempts} attempts Remaining")
        print(levels.hangman_stages[len(levels.hangman_stages)-TotalAttempts])
        TotalAttempts=TotalAttempts-1
   print("You Loose")
   return  
Random_Catogary=random.choice(list(word.Words.keys()))
wword=GetWord(Random_Catogary)
PlayGame()
