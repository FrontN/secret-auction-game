import os
import time
from Secret_Auction_art import logo

def clear_screen():
    """
    Clears the screen and prints the logo.

    This function uses the `os.system` function to clear the screen, and
    then prints the logo defined in the `Secret_Auction_art` module.

    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

def get_valid_int(prompt):
    """
    Prompts the user to enter a valid integer and returns the input as an int.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_input(prompt, options):
    """
    Prompts the user to enter a valid input from a given set of options and returns the input as a string.

    Args:
        prompt (str): The prompt to display to the user.
        options (list): A list of valid inputs.

    Returns:
        str: The valid input entered by the user.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following options: {','.join(options)}")

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

def main():
    """
    This is the main function of the program. It clears the screen, prints
    a welcome message, and then enters a loop where it prompts the user
    to enter their name and bid. It then adds the name and bid to a
    dictionary, and continues to do so until the user decides to
    stop. Finally, it prints out the winner and their bid amount.

    Returns:
        None
    """
    clear_screen()
    print("Welcome to the secret Auction")
    time.sleep(1.5)
    bidders = {}
    keep_going = True

    while keep_going:
        clear_screen()
        name = input("Please enter your name: ")
        clear_screen()
        print(f"Welcome {name}".center(50, "*"))
        bidders[name] = get_valid_int("How much do you want to bid?: ")

        clear_screen()
        if  get_valid_input("Are there any other bidders? Type 'yes' or 'no'.\n", ['yes', 'no', 'y', 'n']).startswith('n'):
            clear_screen()
            find_highest_bidder(bidders)
            keep_going = False
            print("Goodbye!")

if __name__ == "__main__":
    main()
