from ProgramExerciseHF import Food

list = []
def item():
    order = int(input("How many items will you order today? "))
    while order < 1:
        print("Number of items must be at least 1.")
        order = int(input("How many items will you order today? "))
    for i in range(order):
        print(f"Item #{i+1}")
        Foodname = (input(f"Enter food : "))
        TotalPounds = float(input("Enter amount of pounds: "))
        while TotalPounds <= 0:
            print("Amount of pounds must be greater than 0.")
            TotalPounds = float(input("Enter amount of pounds: "))
        print("")
        food = Food(Foodname, TotalPounds)
        list.append(food)
    return list

def showtotal(lists):
    print("Here's a summary of the items purchased:")
    print("-------------------------------")
    for i in range(len(lists)):
        print(f"Item: {lists[i].getFoodHF()}")
        print(f"Amount ordered: {lists[i].getPoundsHF()}")
        print("Price per pound: ${:.2f}".format(lists[i].getCostHF()))
        print("Price of order: ${:.2f}".format(lists[i].calcCostHF()))

def totalPrices(lists):
    total = 0
    for i in range(len(lists)):
        total += lists[i].calcCostHF()
    print("Total cost: ${:.2f}".format(total))

def main():
    a = item()
    showtotal(a)
    totalPrices(a)

main()