# rock_paper_scissor
A classic game which allows user to play rock-paper-scissor game against the computer
### Installing the library
      pip install random
### Usage
```python

      ###importing the random library
      import random

      ###creating variables to store scores of user and computer
      user_wins = 0
      computer_wins = 0

      ###creating a list of choices for the game
      entries = ["rock", "paper", "scissor"]
      #random_number = random.randint(0, 2)
      #computer_pick = entries[random_number]

      ###checking user input
      while True:
          user_input = input( "Type Rock/Paper/Scissor or Q to quit: ").lower()

          ###checking if user wants to quit
          if user_input == "q":
              break
          if user_input not in entries:
              continue

          ###generating a random number for comuter choice
          random_number = random.randint(0, 2)
          computer_pick = entries[random_number]
          print("Computer picked " + computer_pick + ".")

          ###determine the output of the game based on user and computer inputs
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

       ###print the final output and scores
       print("You won " +str(user_wins)  + " times.")
       print("The computer won " + str(computer_wins) + " times.")

```

      
