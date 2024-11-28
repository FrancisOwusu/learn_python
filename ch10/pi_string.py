from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string +=line
    #remove white space on the left
    pi_string +=line.lstrip()
print(pi_string)
print(len(pi_string))


#working with one miliion files
from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string=''
for line in lines:
    pi_string += lines.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string)) 