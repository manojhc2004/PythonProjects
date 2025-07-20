import random

def gameLogic(player):


    options = ["rock","paper","scissor"]
    computer = random.choice(options)

    if player not in options:
        print( "Invalid! enter try again")
    
    else:
        print("You chose:",player)
        print("Computer chose",computer)
        if player == computer:
            print("<<<Game is Tie<<<")

        elif player == 'rock' and computer == 'scissor':
            print(">>>You Win<<<")

        elif player == 'paper' and computer == 'rock':
            print(">>>You Win<<<")

        elif player == 'scissor' and computer == 'paper':
            print(">>>You Win<<<")
        
        else:
            print("<<<You Lose>>>")
        

def main():
    
    while True:
        player = input("Enter rock,paper,scissor (e for exit): ").lower()
        gameLogic(player)
        if player == "e":
            print('>>>Thank You<<<')
            break

main()



    





    









            
             
            
            


