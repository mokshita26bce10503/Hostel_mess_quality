votes = {}

def vote_dish():

    print("\n====================================")
    print("       NEXT WEEK FOOD VOTING")
    print("====================================")

    dish = input("Enter Dish Name: ")

    if dish not in votes:
        votes[dish] = 0

    votes[dish] += 1

    print("Vote Recorded Successfully!")


def voting_report():

    print("\n====================================")
    print("          VOTING REPORT")
    print("====================================")

    if len(votes) == 0:
        print("No Votes Recorded")
        return

    for dish in votes:

        print(dish, ":", votes[dish], "Votes")
