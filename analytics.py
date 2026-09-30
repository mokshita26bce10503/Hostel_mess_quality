from feedback import feedback_data
from complaints import complaints
from waste import waste_records
from voting import votes


def generate_analytics():

    if len(feedback_data) == 0:
        print("No Data Available")
        return

    taste_total = 0
    quantity_total = 0
    hygiene_total = 0
    presentation_total = 0

    recommend_yes = 0

    for feedback in feedback_data:

        taste_total += feedback["taste"]
        quantity_total += feedback["quantity"]
        hygiene_total += feedback["hygiene"]
        presentation_total += feedback["presentation"]

        if feedback["recommendation"].upper() == "Y":
            recommend_yes += 1

    total = len(feedback_data)

    avg_taste = taste_total / total
    avg_quantity = quantity_total / total
    avg_hygiene = hygiene_total / total
    avg_presentation = presentation_total / total

    satisfaction_rate = (recommend_yes / total) * 100

    print("\n=================================================")
    print("      HOSTEL MESS ANALYTICS REPORT")
    print("=================================================")

    print("Total Feedback Entries :", total)

    print("Average Taste Score :", round(avg_taste, 2))
    print("Average Quantity Score :", round(avg_quantity, 2))
    print("Average Hygiene Score :", round(avg_hygiene, 2))
    print("Average Presentation Score :", round(avg_presentation, 2))

    print("Total Complaints :", len(complaints))
    print("Total Waste Records :", len(waste_records))

    print("Student Satisfaction Rate :",
          round(satisfaction_rate, 2), "%")

    o = (avg_taste +avg_quantity +avg_hygiene +avg_presentation) / 4

    print("Overall Mess Rating :", round(overall, 2))

    if o >= 4:
        print("Status : EXCELLENT")

    elif o >= 3:
        print("Status : GOOD")

    else:
        print("Status : NEEDS IMPROVEMENT")

    print("=================================================")
