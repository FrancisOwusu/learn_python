from pathlib import Path

# Specify the path to the file containing the digits of pi
path = Path('pi_digits.txt')

try:
    # Read the content of the file
    contents = path.read_text()
except FileNotFoundError:
    print("The file 'pi_digits.txt' was not found. Please ensure it is in the correct directory.")
    exit()

# Split the content into lines and construct the pi string
lines = contents.splitlines()
pi_string = ''
for line in lines:
    # Use strip() instead of lstrip() to remove whitespace from both sides
    pi_string += line.strip()

# Prompt the user for their birthday
birthday = input("Enter your birthday, in the form mmddyy: ")

# Check if the birthday is in the pi string
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi.")
else:
    print("Your birthday does not appear in the first million digits of pi.")
