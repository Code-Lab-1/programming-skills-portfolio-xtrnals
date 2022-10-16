userprompt = ("Enter your age: ")
age = int(input(userprompt))

if age <= 3:
    print("Your ticket is free!")
elif age <=12:
    print("Your ticket costs $10")
else:
    print("Your ticket costs 15$")
