from pathlib import Path

userName = input("Enter your name")
path = Path("guest.txt")
path.write_text(userName)
print("File writting is done")