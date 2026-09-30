feedback_data = []


def add_feedback():

    print("\n====================================")
    print("      FOOD QUALITY FEEDBACK")
    print("====================================")

    dish = input("Dish Name: ")

    taste = int(input("Taste Rating (1-5): "))
    quantity = int(input("Quantity Rating (1-5): "))
    hygiene = int(input("Hygiene Rating (1-5): "))
    presentation = int(input("Presentation Rating (1-5): "))

    recommendation = input("Would you like this dish again? (Y/N): ")

    comment = input("Additional Comment: ")

    feedback = {"dish": dish,"taste": taste,"quantity": quantity,"hygiene": hygiene,"presentation": presentation,"recommendation": recommendation,"comment": comment}

    feedback_data.append(feedback)

    print("\nFeedback Submitted Successfully!")


def view_feedback():

    if len(feedback_data) == 0:
        print("\nNo Feedback Available")
        return

    print("\n====================================")
    print("         FEEDBACK REPORT")
    print("====================================")

    for feedback in feedback_data:

        print("\nDish :", feedback["dish"])
        print("Taste :", feedback["taste"])
        print("Quantity :", feedback["quantity"])
        print("Hygiene :", feedback["hygiene"])
        print("Presentation :", feedback["presentation"])
        print("Recommend Again :", feedback["recommendation"])
        print("Comment :", feedback["comment"])

