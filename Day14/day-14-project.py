import random
import os

# Define ASCII art as dictionaries
logo = '''
  ____    _    __  __ _____ _____ ____  _   _ 
 / ___|  / \  |  \/  | ____|_   _/ ___|| | | |
| |  _  / _ \ | |\/| |  _|   | | \___ \| | | |
| |_| |/ ___ \| |  | | |___  | |  ___) | |_| |
 \____/_/   \_\_|  |_|_____| |_| |____/ \___/ 
'''

vs = '''
 _    __
| |  / /___  ___
| | / / __ \/ _ \
| |/ / /_/ /  __/
|___/\____/\___|
'''

data = [
    {
        "name": "Account A",
        "description": "A description for Account A",
        "country": "Country A",
        "follower_count": 1000,
    },
    {
        "name": "Account B",
        "description": "A description for Account B",
        "country": "Country B",
        "follower_count": 2000,
    },
    # Add more accounts as needed
]

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    follower_count = account["follower_count"]
    return f"{name}, a {description}, from {country} with {follower_count} followers"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def main():
    print(logo)
    score = 0

    while True:
        account_a, account_b = random.sample(data, 2)
        
        print(f"Compare A: {display_account(account_a)}.")
        print(vs)
        print(f"Against B: {display_account(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        clear_screen()

        print(logo)
        if check_answer(guess, a_follower_count, b_follower_count):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

if __name__ == "__main__":
    main()
