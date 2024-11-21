name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Assign input value to another variable
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")


# Type Casting
age = input("How old are you? ")
age = int(age)
if age > 3:
    print("Number is greater than 3")
else:
    print("your age is less than 2")
