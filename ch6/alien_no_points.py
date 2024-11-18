alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# If the key 'points' exists in the dictionary, you’ll get the
# corresponding value. If it doesn’t, you get the default value.
# In this case, points doesn’t exist, and we get a clean
# message instead of an error:

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)