
# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]

# def largest(lst):
#     _max = 0
#     for num in lst:
#         if num >_max:
#             _max = num
#     print(_max)
# largest(numbers)

# def _sum(lst):
#     result = 0
#     for num in lst:
#         result+=num
#     return result 



# def average(lst):
#     _averageSum = _sum(lst = lst)
#     _average = _averageSum/len(lst)
#     return _average

# print(average(numbers))
# sum/no of items

# def prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# print(prime(7))

# numbers = [15, 27, 10, 12, 10, 6, 28,
#             2, 25, 4,11,17]
# for num in numbers:
#     if prime(num):
#         print(f'{num} is prime')


# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result*=i
#     return result

# print(factorial(10))




# def fib(n):
#     a = 1
#     b = 1
#     for  i in range(n):
#         c = a+b
#         a,b = b,c
#         print(c)
# fib(10)


# numbers = [15, 27, 10, 12, 10, 6, 28,
#             2, 25, 4,11,17]
# def even(lst):
#     _even = []
#     for num in lst:
#         if num %2 ==0:
#             _even.append(num)
#     return _even
# print(even(numbers))




# def palindrome(string):
#     if string == reverse(string=string):
#         return True
#     return False
# print(palindrome('civicds'))

# def reverse(string):
#     return string[::-1]
# def _bin(n):
#     string = ''

#     while True:
#         if n>=1:
#             if n%2 == 0:
#                 string+='0'
#                 n = n//2
#             else:
#                 string +='1'
#                 n = n//2
#         else :
#                 break
#     return reverse(string)
            
# print(_bin(10))
    
# 1 , 1 , 1 , 1
# 16, 8 , 4  ,2
# 2**4 = 16,
# 2**3 = 8


# (n-1) -> 1


# 7 => 7,6,5,4,3,2,1
# 6 => 6,5,4,3,2,1



# def even(lst):
#     _even = []
#     for num in lst:
#         if num %2 ==0:
#             _even.append(num)
#     return _even
# def _sum(lst):
#     result = 0
#     for num in lst:
#         result+=num
#     return result 
# def sum_even(lst):
#     _evens = even(lst = lst)
#     _evenSum = _sum(_evens)
#     return _evenSum

    
# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]
# print(sum_even(lst = numbers))


# user = input('Enter A string: ')
# print(user)
# def largest(lst):
#     _max = 0
#     for num in lst:
#         if num >_max:
#             _max = num
#     return (_max)
# def smallest(lst):
#     _min = float('inf')
#     for num in lst:
#         if num < _min:
#             _min = num
#     return _min

# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]

# print(f'Largest = {largest(lst = numbers)} and smallest = {smallest(lst= numbers)}')
# def words(string):
#     n = string.count(' ')
#     return n+1
# print(words('The quick brown fox jumps over the lazy dog.'))

# def prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True
# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4,11,7,19]
# p = filter(prime,numbers)
# print(list(p))

# def alpha(sentence):
#     words = sentence.split(' ')
#     words.sort()
#     return words
# words = alpha('The quick brown fox jumps over the lazy dog.')
# for word in words:
#     print(word)

# def prod(lst):
#     result = 1
#     for num in lst:
#         result*= num
#     return result
# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]
# print(prod(numbers))

# def solution(string):
#     alpha = 0
#     digit = 0
#     for char in string:
#         if char.isalpha():
#             alpha+=1
#         elif char.isdigit():
#             digit += 1
#     print(f'digits = {digit}, alpha = {alpha}')
# solution('18)Write a Python program that accepts a string and calculates the number of digits and letters in the string. The program should print out the number of digits and letters in the string.')
# def vowels(string):
#     vowels = 'aeiou'
#     vowelsCount = 0
#     for char in string:
#         if char in vowels:
#             vowelsCount+=1
#     return vowelsCount
# print(vowels('The quick brown fox jumps over the lazy dog.'))


# def secondlargest(lst):
#     _max = 0
#     for num in lst:
#         if num >_max:
#             _max = num
#     lst.remove(_max)
#     __max = 0
#     for num in lst:
#         if num >__max:
#             __max = num    
#     return (__max)
# numbers = [15, 27, 10, 12, 10, 6, 28, 2, 25, 4]

# print(secondlargest(lst=numbers))
