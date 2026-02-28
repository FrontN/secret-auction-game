# secret-auction-game
🕵️‍♂️ Secret Auction ProgramA blind auction console application where multiple users can place bids privately. The program clears the screen between bidders to ensure total secrecy, and identifies the winner once all bids are placed.
📖 DescriptionThe Secret Auction is a classic programming challenge that demonstrates the power of Dictionaries and Flow Control in Python. Unlike a traditional auction where bids are public, this program stores data internally and only reveals the highest bidder at the very end.
Key Features:
Encapsulated Logic: Uses a dedicated function find_highest_bidder to process results.
Dictionary Mapping: Efficiently maps unique names (keys) to bid amounts (values).
Screen Clearing: Utilizes the os module to wipe the terminal after each entry, preventing other participants from seeing previous bids.
Input Validation Loop: Features a nested while loop to ensure users provide valid "yes/no" responses.
🛠️ Technical Breakdown
How it Works:
Data Collection: The program prompts for a name and a bid price.
Storage: The data is added to a dictionary: bidders[name] = bid.
The "Blind" Mechanism: The console is cleared using os.system('cls') (Windows) or clear (Linux/Mac).
The Winner Calculation: The program iterates through the dictionary in $O(n)$ time complexity to find the maximum value.
Mathematical Logic:
The algorithm follows a linear search pattern:
winner = max(bids.values())
💻 Installation & Usage
Clone the repository:
Navigate to the directory:
Run the application:
🧪 Example
🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the .
Pro-Tip for your GitHub:
Since you are using a custom module Secret_Auction_art for the logo, make sure that file is also in your repository, otherwise, the code will throw an ImportError.
