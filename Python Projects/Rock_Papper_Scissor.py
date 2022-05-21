        #    >>> ROCK, PAPER, SCISSOR GAME <<<

import random
def Game_Win(computer, You_Turn):
    if computer ==You_Turn:
        return None
    elif computer=='r':
        if You_Turn=='p':
            return True
        elif You_Turn=="s":
            return False
    elif computer =='p':
        if You_Turn=="r":
            return False
        elif You_Turn == "s":
            return True
    elif computer == "s":
        if You_Turn == "r":
            return True
        elif You_Turn == "p":
            return False

print("Computer Turn: Please choose Rock(r), Paper(p) or Sicssor(s): ")
randNo = random.randint(1,3)
if randNo==1:
    computer = 'r'
if randNo==2:
    computer = 'p'
if randNo==3:
    computer = 's'
You_Turn = input("Your Turn: Please choose Rock(r), Paper(p) or Sicssor(s): ")

Result = Game_Win(computer, You_Turn)

print(f"Computer Choose: {computer}")
print(f"You Choose: {You_Turn}")
if Result == None:
    print("The Game is Tie:")
elif Result == True:
    print("You Win the Game:")
elif Result == False:
    print("You loose the Game:")

