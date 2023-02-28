
# def largest(_list):
#     _max = float('-inf')
#     for num in _list:
#         if num > _max:
#             _max = num
#     return _max
# print(largest(numbers))

# print(_sum(numbers))
# def _sum(_list):
#     result = 0
#     for num in _list:
#         result += num
#     return result
# def average(_list):
#     _listSum = _sum(_list)
#     _listlength = len(_list)
#     return _listSum/_listlength
# print(average(numbers))

# def prime(n):
#     for num in range(2,n):
#         if n%num == 0:
#             return False
#     return True  
# print(prime(6))

# def fact(n):
#     result = 1
#     for num in range(1,n+1):
#         result *= num
#     return result
# print(fact(4))
#1 -> n

# def fib(n):
#     a = 1
#     b = 1
#     for i in range(n+1):
#         c = a+b
#         a,b = b,c
#         print(c)
# fib(10)
# def even(n):
#     if n%2 == 0:
#         return True
#     return False
# _evens = []
# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]
# for num in numbers:
#     if even(num):
#         _evens.append(num)
# print(_evens)


# print(reverse(numbers))

# def reverse(string):
#     return string[::-1]

# def palindrome(string):
#     if string == reverse(string = string):
#         return True
#     return False
# print(palindrome('hanzala'))


# 16
# 16/2 = 0
# 8/2 =0
# 4/2 = 0
# 2/2 = 0
# 1/2 = 1

# 1 0 0 0 0

# 16,8,4,2,1




# def reverse(string):
#     return string[::-1]

# def _bin(number):
#     string = ''
#     while True:
#         if number >= 1:
#             if number % 2 == 0:
#                 string +='0'
#                 number = number/2
#             else:
#                 string+='1'
#                 number = number//2
#         else:
#                 break
#     return reverse(string)
# print(_bin(28))








# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]

# def evenSum(_list):
#     _sum = 0
#     for num in numbers:
#         if num%2 !=0:
#             _sum+= num
#     return _sum

# print(evenSum(numbers))

# string = input('Enter your Name: ')
# print(f'hi {string}!')


# def largest(_list):
#     _max = float('-inf')
#     for num in _list:
#         if num > _max:
#             _max = num
#     return _max
# def smallest(_list):
#     _min = float('inf')
#     for num in _list:
#         if num < _min:
#             _min = num
#     return _min

# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]

# _largest =  largest(numbers)
# _smallest = smallest(numbers)
# print(f'THe largest is {_largest} and the smallest = {_smallest}')

# def countWord(sentence:str):
#     words = sentence.count(' ') + 1
#     return words


# print(countWord('The quick brown fox jumps over the lazy dog.'))

# def prime(n):
#     for num in range(2,n):
#         if n%num == 0:
#             return False
#     return True 


# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4,3,11,17]

# primes = []
# for  num in numbers:
#     if prime(num):
#         primes.append(num)

# def _filter(function,iterable):
#     result = []
#     for _iter in iterable:
#         if function(_iter):
#             result.append(_iter)
#     return result

# primes = _filter(prime,numbers)
# print(primes)

# def alphOrder(sentence:str):
#     words = sentence.split(' ')
#     words.sort()
#     for word in  words:
#         print(word)
# alphOrder('The quick brown fox jumps over the lazy dog.')
# def prod(_list):
#     result = 1
#     for num in _list:
#         result = result * num
#     return result
# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]
# print(prod(numbers))

# def count(sentence):
#     alpha = 0
#     digit = 0
#     for char in sentence:
#         if char.isalpha():
#             alpha+=1
#         elif char.isdigit():
#             digit+=1
#     print(f'alphbets = {alpha}, digits = {digit}')
# count('18)Write a Python program that accepts a string and calculates the number of digits and letters in the string. The program should print out the number of digits and letters in the string.')



# def vowelsCount(sentence):
#     vowels = 'aeiou'
#     count = 0
#     for char in sentence:
#         if char in vowels:
#             count+= 1
#     return count
# print(vowelsCount('The quick brown fox jumps over the lazy dog'))


def largest(_list):
    _max = float('-inf')
    for num in _list:
        if num > _max:
            _max = num
    return _max

numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]

_largest = largest(numbers)
numbers.remove(_largest)
second_largest = largest(numbers)
print(second_largest)