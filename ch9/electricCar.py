from ch9.battery import Battery
from ch9.car import Car

"""Inheritance"""
class ElectricCar(Car):
    """Represent aspects of a car,specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # method overriding
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

my_leaf.battery.battery_size()
my_leaf.battery.get_range()
