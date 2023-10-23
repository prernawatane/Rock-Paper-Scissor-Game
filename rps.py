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
game_image = [rock, paper, scissors]
user_choice = int(input("What do you choose?Type 0 for rock, 1 for paper,and 2 for scissor\n"))
print(game_image[user_choice])
computer_choice = random.randint(0, 2)
print( f"computer chose:",game_image[computer_choice])

if user_choice>3 or computer_choice<0:
    print("You have entered invalid choice")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice==2 and computer_choice==0:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice >computer_choice:
    print("You win")
elif user_choice == computer_choice:
    print("Its a draw")
