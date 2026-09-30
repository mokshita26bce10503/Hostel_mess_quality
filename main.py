from feedback import *
from complaints import *
from waste import *
from voting import *
from analytics import *

while True:
    print("=" * 60)
    print(" HOSTEL MESS QUALITY ASSESSMENT AND ANALYTICS SYSTEM ")
    print("=" * 60)

    print('''1. Submit Food Feedback
    2. View Feedback Report
    3. Submit Complaint
    4. View Complaint Report
    5. Add Waste Record
    6. View Waste Report
    7. Vote For Preferred Dish
    8. View Voting Report
    9. Generate Analytics Report
    10. Exit''')
    print("=" * 60)

    c = int(input("Enter your choice : "))

    if c == 1:
        add_feedback()

    elif c == 2:
        view_feedback()

    elif c == 3:
        add_complaint()

    elif c == 4:
        view_complaints()

    elif c == 5:
        add_waste()

    elif c == 6:
        waste_report()

    elif c == 7:
        vote_dish()

    elif c == 8:
        voting_report()

    elif c == 9:
        generate_analytics()

    elif c == 10:
        print("Thank You For Using The System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
