sandwich_orders = ["Chicken", "Egg", "Nutella", "Grilled Cheese", "Ham"]
finished_sandwiches = []

while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print(preparing_sandwich + " Sandwich is being prepared.")
    finished_sandwiches.append(preparing_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("Your " + sandwich + " has been made and is ready to go!")
    