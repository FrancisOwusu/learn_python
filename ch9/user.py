class User:
    """Class to model User profile"""

    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def describe_user(self):
        """Describe the user profile."""
        print(
            f"Firstname: {self.first_name} \n Lastname: {self.last_name} \n Age: {self.age} \n Height: {self.height}"
        )

    def greet_user(self):
        print(f"Hello")


user_profile = User("Francis", "Osei", 23, "5feet")
print(f"{user_profile.greet_user()} \n")
print(
    f"************Display  User Profile************ \n{user_profile.describe_user()} \n"
)
