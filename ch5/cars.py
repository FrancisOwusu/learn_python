cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
  if car == 'bmw':
    print(car.upper())
else:
 print(car.title())
 
 
 #  Ignoring Case When Checking for Equality
 for cr in cars:
     if cr.lower() =='audi':
         print(cr)
