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
player_moves = input("Your move: ROCK/PAPER/SCISSORS:\n")
player_moves_L = player_moves.lower()
computer = [rock,paper,scissors]
computer_turn = random.choice(computer)

if player_moves_L=="rock" and computer_turn==scissors:
  print("Your move\n" ,rock)
  print("Computer move\n",computer_turn)
  print("YOU WIN!")
elif player_moves_L=="rock" and computer_turn==paper:
  print("Your move\n" ,rock)
  print("Computer move\n",computer_turn)
  print("YOU LOSS")
elif player_moves_L=="paper" and computer_turn==scissors:
  print("Your move\n" ,paper)
  print("Computer move\n",computer_turn)
  print("YOU LOSS")
elif player_moves_L=="paper" and computer_turn==rock:
  print("Your move\n" ,paper)
  print("Computer move\n",computer_turn)
  print("YOU WIN!")
elif player_moves_L=="scissors" and computer_turn==paper:
  print("Your move\n" ,scissors)
  print("Computer move\n",computer_turn)
  print("YOU WIN!")
elif player_moves_L=="scissors" and computer_turn==rock:
  print("Your move\n" ,scissors)
  print("Computer move\n",computer_turn)
  print("YOU LOSS")
else:
  
  print("TIE")
