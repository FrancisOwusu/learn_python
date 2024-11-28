from pathlib import Path

# Initialize an empty string to collect all user names
user_names = ""
while True:
    
   # Prompt the user for their name
    user_name = input("Enter your name (or 'quit' to exit): \n")
    
    # Check if the user wants to quit
    if user_name.lower() == "quit":
        break
  
    # Accumulate the entered name in the user_names string with a newline
    user_names += user_name + "\n"
  
path = Path("guest_book.txt")
path.write_text(user_names)
