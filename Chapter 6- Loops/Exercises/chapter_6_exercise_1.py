userprompt = "\nEnter the toppings you would like to add on your pizza: "
userprompt += "\nType 'quit' once you're done with your toppings: "

while True:
    pizza = input(userprompt)
    if pizza != 'quit':
        print("We'll add" + pizza + "to your pizza!")
    else:
        break