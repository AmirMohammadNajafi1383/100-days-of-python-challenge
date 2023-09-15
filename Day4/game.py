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

import random 
def get_user_choice():
  user=(input("Enter your choice (rock, paper, or scissors): ")).lower()

  while user not in ['rock','paper','sicssors']: 
    print('invalid') 
    
  user_choice=input('Enter your choice (rock, paper, or scissors):').lower()
  return user_choice


def get_computer_choice():
  choice=['rock','paper','scissors']
  return random.choice(choice)


def game_of_win(user_choice ,computer_choice):
  if user_choice == computer_choice :
    print ('Its tie')
  elif (
    (user_choice =='rock' and computer_choice =='scissors')or
    (user_choice == 'paper' and computer_choice =='rock') or
    (user_choice == 'scissors' and computer_choice == 'paper')
  ):
    print('Its win ')
  else: 
    print('computer wins') 

def play_game():
  print('start the game ')
  while True :
    user_choice=get_user_choice()
    computer_choice=get_computer_choice()
    print(f'user_choice {user_choice}')
    print(f'computer_choice {computer_choice}')
    result= game_of_win(user_choice ,computer_choice)
    print(result)
    play_again = input("Play again? (yes/no): ").lower()   
    if play_again != 'yes':    
            break
    
if __name__ == '__main__':
   play_game()

  
  
  