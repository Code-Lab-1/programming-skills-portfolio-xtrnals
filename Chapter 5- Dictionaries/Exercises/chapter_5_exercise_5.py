pets = []

pet = {
    'animal' : 'dog',
    'name' :  'kimi',
    'owner' : 'johnny',
}
pets.append(pet)

pet = {
    'animal' : 'cat',
    'name' : 'kit',
    'owner' : 'khan'
}
pets.append(pet)

pet = {
    'animal' : 'parrot',
    'name' : 'rosy',
    'owner' : 'anthony',
}
pets.append(pet)

for pet in pets:
    print("\nInformation: " + pet['name'].title())
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))