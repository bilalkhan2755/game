import random

paper='''
_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor=''' 
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissor]
user_choice=int(input("what do you want to choose?type 0 to rock ,1 to paper and 2 to scissor?\n"))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])

computer_choice=random.randint(0,2)
print("computer_choice:")
print(game_images[computer_choice])

if user_choice>=3 and computer_choice<0:
    print("it is invalid intax.you lose!")
elif computer_choice==0 and user_choice==2:
    print("you lose!")
if computer_choice==2 and user_choice==0:
    print("you win!")
elif computer_choice>user_choice:
    print("you lose!")
elif user_choice>computer_choice:
    print("you win!")
elif computer_choice==user_choice:
    print("the game is draw!")

