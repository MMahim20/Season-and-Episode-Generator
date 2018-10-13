from random import *

def rand_season():
  x = randint(1,9)
  return x
def rand_episode():
  y = randint(1,24)
  return y


def season():
  i=0
  while i==0:
    print(f"Season {rand_season()}")
    print("""Would you like to pick another season instead of this, pick an episode, or stop?
  1 for another season
  2 for an episode
  3 to stop.""")
    choice2=input(">") 
    if choice2 == "2":
      episode()
      i = 1
    elif choice2 == "3":
      i = 1
        
def episode():
  j=0
  while j==0:
    print(f"Episode {rand_episode()}")
    print("""Would you like to pick another episode instead of this, pick a season, or stop?
  1 for another episode
  2 for a season
  3 to stop.""")
    choice2=input(">") 
    if choice2 == "1":
      episode()
    elif choice2 == "2":
      season()
      #j = 1
    elif choice2 == "3":
      j = 1
    else:
      #while choice2 != "1" or choice2 != "2" and choice2 != "3":
      f = 0
      while f == 0:
        print("Please choose a valid input.")
        choice2=input(">")
        if choice2 == "1" or choice2 == "2" or choice2 == "3":
          f = 1
        
def main():
  print("""Welcome to the random TV episode generator. Would you like to pick a season or episode? 
  1 for season
  2 for episode.""")
  
  choice = input(">")
  if choice == "1":
    season()
  else:
    episode()
  print("Good bye.")
  
main()

    
      


  
  