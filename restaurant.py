class Restaurant:
    """Class to describe restaurant name and type of cuisine."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints name of the restaurant and type of cuisine"""
        print(f"{self.restaurant_name} is a {self.cuisine_type} type of restaurant")

    def open_restaurant(self):
        """Prints that the restaurant is open"""
        print(f"{self.restaurant_name} is open!")

restaurant = Restaurant('Sabor', 'Latin')

print(f"My restaurant name is {restaurant.restaurant_name} and it's type of cuisine is {restaurant.cuisine_type}")

