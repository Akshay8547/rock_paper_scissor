import random

user_wins = 0
computer_wins = 0
entries = ["rock", "paper", "scissor"]
#random_number = random.randint(0, 2)
#computer_pick = entries[random_number]

while True:
    user_input = input( "Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in entries:
        continue

    random_number = random.randint(0, 2)
    computer_pick = entries[random_number]
    print("Computer picked " + computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissor":
       print("You won!great.")
       user_wins += 1
       continue
    elif user_input == "paper" and computer_pick == "rock":
       print("You won!great.")
       user_wins += 1
       continue
    elif user_input == "scissor" and computer_pick == "paper":
       print("You won!great.")
       user_wins += 1
       continue
    else:
        print("You lost!")
        computer_wins += 1
        
 print("You won " +str(user_wins)  + " times.")
 print("The computer won " + str(computer_wins) + " times.")


      

