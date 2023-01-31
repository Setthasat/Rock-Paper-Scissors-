import random

def main(): 
    Ai = ["rock", "paper", "scissors "]
    player = input("rock, paper, scissors  : ")
    if player == "rock" or player == "paper" or player == "scissors " :
        Play(player, Ai[random.randint(0, 2)])
    else : 
        print('can input only "rock", "paper", "scissors"')

    
def Play(player, Ai) : 
    print("Ai play : ", Ai)
    if player == Ai : 
        print("Tie")
    elif (player == "paper" and Ai == "rock") or (player == "scissors " and Ai == "paper") or (player == "rock" and Ai == "scissors") :
        print("the winner is : player!!")
    else : 
        print("The winner is Ai !!")
        
    
if __name__ == "__main__" :
    main()
