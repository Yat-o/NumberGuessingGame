"""
made by Yato
"""


import random 
attemptslist = []
def show_score():
    if len(attemptslist) <= 0:
        print('There is no highscore')
    else:
        print(f'The current HS is {min(attemptslist)}')

def start_game():
    random_number = int(random.randint(1, 10))
    print('Hello there. Welcome to the number guessing game.')
    player_name = input('what is your name?')
    wanna_play = input(f'Hi, {player_name}, wanna play the game (yes/no)')
    """
    """
    attempts = 0 
    show_score()
    while wanna_play.lower() == 'yes':
        try:
            guess = input('Pick a number between 1 and 10:')
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError('Please Pass In A Valid Value')
            
            if int(guess) == random_number:
                print('Good Job! You Got It!')
                attempts += 1
                print(f'It took you {attempts} attempt')
                play_again = input('Wanna go again? (yes/no)')
                
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == 'no':
                    print('Goodbye!')
                    break
            elif int(guess) > random_number:
                print('Your too high')
            elif int(guess) < random_number:
                print('Your too low')
                attempts += 1
        except ValueError as err:
            print('Pass in a valid value')
            print(err)
    else:
        print('Goodbye')
if __name__ == '__main__':
    start_game()
