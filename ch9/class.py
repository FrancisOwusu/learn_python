"""A Simple attempt to model a dog"""


class Dog:
    """A Simple attempt to model a dog"""

    def __init__(self, name, age):
        """
        initialize name and age attributes
        _summary_

        Args:
            name (_type_): _description_
            age (_type_): _description_
        """
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog("Francis", 45)
print(f"My dog's name is {my_dog.name}.")

print(f"My dog is {my_dog.age} years old.")

# calling methed
my_dog.name
my_dog.age
