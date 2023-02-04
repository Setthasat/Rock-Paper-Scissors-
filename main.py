
import random

def main(): 
    Ai = ["rock", "paper", "scissors"]
    player = input("rock, paper, scissors  : ")
    if player == "rock" or player == "paper" or player == "scissors " or "s" or "r" or "p":
        Play(player, Ai[random.randint(0, 2)])
    else : 
        print('can input only "rock", "paper", "scissors"')
        
def Play(player, Ai) : 
    
# ----------------------------------------------------------------------------- #
    print("Ai play : ", Ai)
    if player == "r" : 
        print("Player Play : rock")
    elif player == "p" : 
        print("Player Play : papper")
    elif player == " s" : 
        print("Player Play : scissors")
    else : 
        print(f"Player play : {player}")
        
# ----------------------------------------------------------------------------- #
    if player == Ai or (player == "r" and Ai == "rock") or (player == "p" and Ai == "paper") or (player == "s" and Ai == "scissors")  : 
        print("Tie")
    elif (player == "paper" or player == "p" and Ai == "rock") or (player == "scissors " or player == "s" and Ai == "paper") or (player == "rock" or player == "r" and Ai == "scissors") :
        print("the winner is : player!!")
    else : 
        print("The winner is Ai !!")
        
    
if __name__ == "__main__" :
    main()
