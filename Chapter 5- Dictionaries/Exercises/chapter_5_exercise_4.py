rivers = {
    'nile' : 'egypt',
    'amazon' : 'peru',
    'yangtze' : 'china',
}

for river, country in rivers.items():
    print("The " + river.title() + " river runs through " + country.title() + '.')

print("\n rivers included:")
for river in rivers.keys():
    print("> " + river.title())

print("countries included:")
for country in rivers.values():
    print("> " + country.title())
