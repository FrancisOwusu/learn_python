"""AI is creating summary for

Returns:
    [type]: [description]
"""


# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    """_summary_

    Args:
        number1 (_type_): _description_
        number2 (_type_): _description_
    """
    # Return the sum of 'number1' and 'number2'.
    # This line computes the addition of the two input numbers and outputs the result.
    return number1 + number2


# Initialize the variable 'num1' with the value 4.
num1 = 4

# Initialize the variable 'num2' with the value 5.
num2 = 5

# Call the 'add' function with 'num1' and 'num2' as arguments and store the result in 'total'.
total = add(num1, num2)

# Print the result of adding 'num1' and 'num2' using the 'format' method to insert the values into the string.
print("The sum of {} and {} is {}".format(num1, num2, total))
