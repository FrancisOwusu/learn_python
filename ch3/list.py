bicycles = ['trek', 'cannondale', 'redline', 'specialized']

for bike in bicycles:
    print(bike)
# print(bicycles)

#return first element
print(bicycles[0])

#return last element
print(bicycles[-1])

# Let’s try pulling the first bicycle from the list and
# composing a message using that value:
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Adding Elements to a List
bicycles.append('ducati')

#Remove Element from a list
del bicycles[1]

# using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping Items from Any Position in a List
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an Item by Value
motorcycles2 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles2)
motorcycles2.remove('ducati')
print(motorcycles2)


# sort list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Finding the Length of a List
len(cars)
