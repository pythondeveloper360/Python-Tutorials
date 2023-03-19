# create a list of square numbers from 1-10
# Messy Approach
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)
# list comprehension
squares = [i**2 for i in range(1,11)]
print(squares)
