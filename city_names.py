def city_country(city, country):
    """Returns name of city and country formatted"""
    city_country = f"{city}, {country}"
    return city_country.title()


# Infinite loop
while True:
    print("\nPlease enter name of a city and its country:")
    print("Enter 'q' at any time to quit")

    ci_name = input("Name of the city: ")
    if ci_name == 'q':
        break

    co_name = input("Name of the country: ")
    if co_name == 'q':
        break

    formatted_city = city_country(ci_name, co_name)
    print(f"\n{formatted_city}")