famous_rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'ozama': 'dominican republic'
}

for rivers in famous_rivers.values():
    print(rivers.title())

for cities in famous_rivers.keys():
    print(cities.title())

for rivers, cities in famous_rivers.items():
    print(f"The {rivers.title()} is located in the country of {cities.title()}")