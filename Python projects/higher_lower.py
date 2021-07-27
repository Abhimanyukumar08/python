from HigherLower_data import data
import random
import os
clear = lambda:os.system('cls')
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

#Generate the random account from higher lower data
def get_random_choice():
    return random.choice(data)

def format_account(account):
    '''format the account into printable format '''
    name = account["name"]
    des = account["description"]
    c = account["country"]
    return (f"{name},a {des},from {c}")
def correct_guess(guess,a,b):
    '''check if the guess is correct or not'''
    if a>b:
        return guess =="a"
    else:
        return guess =="b"

def game():      
    account_a = get_random_choice()
    account_b = get_random_choice()
    game_Should_continue = True
    score = 0
    while game_Should_continue:
        account_a = account_b
        account_b = get_random_choice()

        while account_a==account_b:
            account_b = get_random_choice()
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has the more follwers? Type 'A' or 'B' :").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        correct_guess(guess,a_follower_count,b_follower_count)
        clear()
        print(logo)
        if correct_guess:
            score +=1
            print(f"You are right, score is {score}")
        else:
            game_Should_continue=False
            print(f"Sorry that's wrong,Final score is{score} ")

game()