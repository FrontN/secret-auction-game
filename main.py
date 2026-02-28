import os
from Secret_Auction_art import logo
print(logo)
print("Welcome to the secret Auction")

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    """
    This function takes a dictionary of bidders and their bids, and returns
    a string declaring the winner and their bid amount.

    Parameters:
        bidding_record (dict): A dictionary where the keys are the names of the
            bidders and the values are their respective bids.

    Returns:
        str: A string declaring the winner and their bid amount.
    """
    highest_bid = 0
    winner = ""
    for x in bidding_record:
        if bidding_record[x] > highest_bid:
            highest_bid = bidding_record[x]
            winner = x
    print(f"The winner is: {winner} with a bid of: {highest_bid}")

bidders = {}
keep_going = True

while keep_going:
    name = input("Please enter your name: ")
    bid = int(input("How much do you want to bid?: "))
    bidders[name] = bid

    new_bidder = True
    while new_bidder:
        next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
        if next_bidder == 'yes':
            clear_screen()
            print(logo)
            new_bidder = False
        elif next_bidder == 'no':
            clear_screen()
            print(logo)
            find_highest_bidder(bidders)
            keep_going = False
            new_bidder = False
        else:
            print("Opzione non valida")