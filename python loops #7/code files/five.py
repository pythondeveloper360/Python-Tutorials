# # loops
# for letter in ['c','a','t']:
# 	print(letter)

# print(letter)

# num = 0
# numbers = [3,5,9,-1,3,1]
# for number in numbers:
#     if number < 0:
#         print(number)
#         break
#     num +=number #num = num+number
# print(num)

# num = 0
# numbers = [3,5,9,-1,3,1]
# for number in numbers:
#     if number<0:
#         print(number)
#         continue
#     num+=number
# print(num)

# animals = ['cat','dog','bird']
# print('dogy' in animals)



# names = ['john','paul','george','ringo']
# for name in names:
# 	if name not in ['john','paul']:
# 		names.remove(name)
# print(names)
# names = ['john','paul','george','ringo']

# print(names)
# namesToRemove = []

# for name in names:
#     if name not in ['john','paul']:
#         namesToRemove.append(name)

# for name in namesToRemove:
#     names.remove(name)
# print(names)


# names = ['john','paul',"paul",'george','ringo']
# print(names)
# namescopy = names.copy()

# for name in namescopy:
#     if name in ['john','paul']:
#         names.remove(name)
# print(names)


# names = ['john','paul','george','ringo']

# for name in names:
#     if name == 'paul':
#         continue
#     print(name)
# else:
#     print('else clause')

# while True:
#     print('hanzala')


# n=5
# while n>=0:
#     print(n)
#     n-=1 # n = n-1
# n=5
# while True:
#     print(n)
#     n-=1
#     if n<=0:
#         break


# marks = [90,80,70,67,89,78]
# _sum = 0
# for mark in marks:
#     _sum+=mark
# print(_sum)

# print('the average is ',_sum/len(marks))



names = ['john','paul','george',
        'ringo','hamza','saad']
userinput = input('Enter the name: ')
found = False
for name in names:
    if userinput == name:
        found = True
        print('it is on the index',names.index(name))
if not found :
    print('It is not there')










