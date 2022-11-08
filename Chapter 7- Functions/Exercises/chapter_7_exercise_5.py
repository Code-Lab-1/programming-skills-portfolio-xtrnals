def describe_city(city, country="United Arab Emirates"):
    text = city.title() + " is in " + country.title() + "."
    print (text)

describe_city('Dubai')
describe_city('Paris', 'France')
describe_city('Abu Dhabi')