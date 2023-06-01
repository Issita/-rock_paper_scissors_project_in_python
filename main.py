# Rock Paper Scissors
import random #module

def gameWin(comp, you):
    # if two values are equal, declare tie
    if comp == you:
        return None
    
    # check for all possibilities when computer choose r
    elif comp == "r":
        if you == "s":
             return False
        elif you == "p":
            return True
    # check for all possibilities when computer choose p
    elif comp == "p":
        if you == "r":
             return False
        elif you == "s":
            return True
    # check for all possibilities when computer choose s
    elif comp == "s":
        if you == "p":
             return False
        elif you == "r":
            return True

print("Comp Turn: Rock(r) Paper(p) or Scissors(s)?")
randNo = random.randint(1, 3) #randint is a function of random module
if randNo ==1:
    comp = "r"
elif randNo ==2:
    comp = "p"    
elif randNo ==3:
    comp = "s"
you = input("Your Turn: Rock(r) Paper(p) or Scissors(s)?")
a = gameWin(comp, you)
print(f"Computer choose {comp}")# choose variable in curly brases
print(f"you choose {you}")
if a == None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
    