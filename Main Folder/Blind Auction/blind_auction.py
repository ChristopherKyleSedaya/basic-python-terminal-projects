from art import logo
print(logo)


bidding = True


bidders = {}

highest_bidder = ""

highest_values = 0

while bidding:

    name = input("What is your name?: ").lower()
    bid = int(input("What is your bid price?: $"))


    bidders.update({name: bid})



    continue_question = input("Do others want to bid? Y/N").lower()

    if continue_question == "y":
        print("\n" * 100)


    elif continue_question == "n":

        for key in bidders:

            if highest_bidder == "":
                highest_bidder = key
                highest_values = bidders[key]

            elif bidders[key] >  highest_values:
                highest_values = bidders[key]


        print(f"{highest_bidder} is the highest bidder! with ${highest_values}")
        bidding = False
