complaints = []

def add_complaint():

    print("\n====================================")
    print("          COMPLAINT PORTAL")
    print("====================================")

    print("1. Taste")
    print("2. Hygiene")
    print("3. Quantity")
    print("4. Variety")

    c = int(input("Choose Category: "))

    if c == 1:
        category = "Taste"

    elif c == 2:
        category = "Hygiene"

    elif c == 3:
        category = "Quantity"

    else:
        category = "Variety"

    description = input("Enter Complaint: ")

    complaints.append({"category": category,"description": description})

    print("\nComplaint Registered!")


def view_complaints():

    if len(complaints) == 0:
        print("\nNo Complaints Available")
        return

    print("\n====================================")
    print("         COMPLAINT REPORT")
    print("====================================")

    for complaint in complaints:

        print("\nCategory :", complaint["category"])
        print("Issue :", complaint["description"])
