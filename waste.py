waste_records = []

def add_waste():

    print("\n====================================")
    print("         WASTE MONITORING")
    print("====================================")

    dish = input("Dish Name: ")
    served = int(input("Students Served: "))
    waste = float(input("Waste Generated (Kg): "))

    waste_records.append({
        "dish": dish,
        "served": served,
        "waste": waste
    })

    print("\nWaste Data Recorded!")


def waste_report():

    if len(waste_records) == 0:
        print("\nNo Waste Records")
        return

    print("\n====================================")
    print("           WASTE REPORT")
    print("====================================")

    for record in waste_records:

        print("\nDish :", record["dish"])
        print("Students Served :", record["served"])
        print("Waste :", record["waste"], "Kg")
