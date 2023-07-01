#slice list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# You can generate any subset of a list. For example, if you
# want the second, third, and fourth items in a list, you would
# start the slice at index 1 and end it at index 4:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# If you omit the first index in a slice, Python automatically
# starts your slice at the beginning of the list:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# if you want all items from the
# third item through the last item, you can start with index 2
# and omit the second index:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

# For example, if we
# want to output the last three players on the roster, we can
# use the slice players[-3:]:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")

for player in players[:3]:
  print(player.title())