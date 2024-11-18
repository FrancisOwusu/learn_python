user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

# loop in dictionary 
for key, value in user_0.items():
 print(f"\nKey: {key}")
print(f"Value: {value}")

# for k, v in user_0.items()


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name, language in favorite_languages.items():
 print(f"{name.title()}'s favorite language is {language.title()}.")
 
#  loop through all keys in dictionary
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name in favorite_languages.keys():
 print(name.title())
 
#  Looping through the keys is actually the default behavior
# when looping through a dictionary, so this code would have
# exactly the same output if you wrote:
# for name in favorite_languages:

favorite_languages = { 'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python', }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
 print(f"Hi {name.title()}.")
if name in friends:  language = favorite_languages[name].title()
print(f"\t{name.title()}, I see you love {language}!")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'erin': 'python',
}
if 'erin' not in favorite_languages.keys():
 print("Erin, please take our poll!")
 
#  Looping Through a Dictionary’s Keys in a
# Particular Order

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
 print(f"{name.title()}, thank you for taking the poll.")
 
 
 favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())
 
#  Looping Through All Values in a Dictionary

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())
 
#  To see
# each language chosen without repetition, we can use a set.
# A set is a collection in which each item must be unique:
 print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
 print(language.title())
 
 #direct set
 languages = {'python', 'rust', 'python', 'c'}
print(languages)
