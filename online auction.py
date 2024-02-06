logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                     /_______________\
'''
print(logo)
bids = { }
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = " "
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("Enter your name?")
    price = int(input("Enter your bidding price? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if should_continue == "no":
        bidding_finished = True
        print("Thank you for using online auction!....")
    else:
        # clear the cansole
        bidding_finished = False
    find_highest_bidder(bidding_record=bids)