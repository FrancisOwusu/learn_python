# For example, consider how you
# might make a list of the first 10 square numbers (that is, the
# square of each integer from 1 through 10). In Python, two
# asterisks (**) represent exponents. 

squares = []
for value in range(1, 11):
  square = value ** 2
  squares.append(square)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
# List Comprehensions

squares = [value**2 for value in range(1, 11)]
print(squares)