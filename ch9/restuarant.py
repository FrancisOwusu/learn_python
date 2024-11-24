class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"{self.restaurant_name} offers {self.cuisine_type} cuisine.")


# Create an instance of the Restaurant class
my_restaurant = Restaurant("KFC", "PIZZA ")

# Call the describe_restaurant method and print the cuisine type
my_restaurant.describe_restaurant()
print(
    f"My restaurant is called {my_restaurant.restaurant_name} and it offers {my_restaurant.cuisine_type}."
)

my_restaurant2 = Restaurant("Papaye", "Fried Rice")
my_restaurant2.describe_restaurant()
print(
    f"My restaurant is called {my_restaurant2.restaurant_name} and it offers {my_restaurant2.cuisine_type}."
)

my_restaurant3= Restaurant("Samesh Ventures","Banku and Kenkey")
my_restaurant3.describe_restaurant()
print(
    f"My restaurant is called {my_restaurant2.restaurant_name} and it offers {my_restaurant2.cuisine_type}."
)
