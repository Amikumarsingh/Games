print("WELCOME TO ROCK PAPER SCISSOR GAME!")
import random
Rock=('''

    ______
---'  ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
scissor =('''

            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
''')
paper=('''

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
game_images =[Rock, paper, scissor]
user_input =int(input("What do you choose? Type 0 for rock, 1 for paper ,2 for scissor?\n"))
computer_input= random.randint(0,2)
if user_input >= 3 or user_input< 0:
    print("you typed a invalid number, you loose")
else:
     print(game_images[user_input])
     print('computer choice :')
     print(game_images[computer_input])
     if user_input == 0 and computer_input == 2:
         print("you won!")
     elif user_input == 2 and computer_input == 0:
         print("you loose!")
     elif computer_input > user_input:
         print("You won!")
     elif user_input > computer_input:
         print("You loose!")
     elif user_input == computer_input:
         print("Match drawn!")
