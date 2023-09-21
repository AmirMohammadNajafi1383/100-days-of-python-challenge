import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bid(bids_dict):
    highest_bid = 0
    highest_bidder = None

    for name, bid in bids_dict.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = name

    return highest_bid, highest_bidder

print('Welcome to the secret auction program')

bids = {}  # Store bids as a dictionary

while True:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    soul = input("Are there any other bidders? Type 'yes' or 'no': ")

    if soul.lower() == 'yes':
        clear_screen()
    elif soul.lower() == 'no':
        break

    bids[name] = bid  # Store the bid in the dictionary with the name as the key

highest_bid, highest_bidder = find_highest_bid(bids)

clear_screen()
print(f"The highest bid is ${highest_bid} from {highest_bidder}")
