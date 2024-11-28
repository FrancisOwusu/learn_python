from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
#remove blank space

#You can use the splitlines() method to turn a long string into a set of lines
lines = contents.splitlines()

contents = contents.rstrip()
print(contents)

for line in lines:
    print(line)
    
