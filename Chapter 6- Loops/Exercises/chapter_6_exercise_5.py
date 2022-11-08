sandwich_orders = ["Chicken", "Egg", "Nutella", "Grilled Cheese", "Ham", "Pastrami", "Pastrami", "Pastrami"]
finished_sandwiches = []

print("We have ran out of pastrami for today, sorry for the inconvenience!")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

print("\n")
while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print(preparing_sandwich + " Sandwich is being prepared.")
    finished_sandwiches.append(preparing_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("Your " + sandwich + " has been made and is ready to go!")
    