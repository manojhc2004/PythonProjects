import random


class Number_Guess:

    def guess(self):
        computer =( random.randint(1,100))
        
        while True:
            player = input("Enter a number b/w 100-1 (e for exit):").lower()
            if player =="e":
                print("Thank You😊")
                break
            
            elif not player.isdigit():
                print("Invalid Enter!⚠️")

            else:
                if int(player) > computer:
                    print(" ↑ Too High ↑")
                elif int(player) < computer:
                    print(" ↓ Too Low ↓")
                else:
                    print("🎉You Win🎉")


start_game = Number_Guess()
start_game.guess()
