import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Angela code

game_images = [rock, paper, scissors] # Make a list to easily call game_images[computer_choice] for user and computer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))


# Check if there is an invalid response first. Do not refernece print(game_images[user_choice]) here because the number will be out of range. That must be put in the else block after filtering out any incorrect values.

if user_choice >= 3 or user_choice < 0: # Must be first because if user_choice > computer_choice and this isnt called, then it will say I won when I entered a large invalid number
  print("This is not a valid option.") 
else:
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])
  
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("Its a draw")


# Original Code I made

# player_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
# computer_decision = random.randint(0,2) 

# if player_decision == 0:
#   print(f"You chose {rock}\n")
#   if computer_decision == 0:
#     print(f"Computer chose {rock}\n You chose rock. Game ends in a tie.")
#   elif computer_decision == 1:
#     print(f"Computer chose {paper}\n Paper beats rock. You lose.")
#   else:
#     print(f"Computer chose {scissors}\n Rock beats scissors. You win.")
# elif player_decision == 1:
#   print(f"You chose {paper}\n")
#   if computer_decision == 0:
#     print(f"Computer chose {rock}\n paper beats rock. You win!")
#   elif computer_decision == 1:
#     print(f"Computer chose {paper}\n Game ends in a tie.")
#   else:
#     print(f"Computer chose {scissors}\n Scissors beats paper. You lose.")
          
# elif player_decision == 2:
#   print(f"You chose {scissors}\n")
#   if computer_decision == 0:
#     print(f"Computer chose {rock}\n Rock beats scissors. You lose")
#   elif computer_decision == 1:
#     print(f"Computer chose {paper}\n Scissors beats paper. You win!")
#   else:
#     print(f"Computer chose {scissors}\n You chose scissors. Game ends in a tie.")
# else:
#   print("That was not a supported option.")