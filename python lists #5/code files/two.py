# lists

        #  0,1,2,3,4,5,6
# numbers = [2,3,4,5,6,7,8,0,0]
# # print(numbers)

# #append
# numbers.append(9)
# # print(numbers)

# numbers.insert(0,1)
# # print(numbers)
# print(numbers)

# #remove
# numbers.remove(0)
# print(numbers)

#sort
# numbers = [9,5,6,3,62,5]
# numbers.sort(reverse=True)
# print(numbers)

# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[0])
# print(numbers[1::2])

# range
odd = list(range(1,10,2))
even = list(range(0,10,2))
numbers = odd+even
numbers.sort()
print(numbers)

# dunder functions
# print(['a'].__add__(['b']))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# for loops

for number in numbers:
    print(number+2)
