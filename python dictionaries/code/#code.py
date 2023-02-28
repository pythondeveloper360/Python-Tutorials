# capitals = dict(Pakistan = 'Islamabad',USA = 'Washington DC',Enland = 'London')
# print(capitals)
# mapping  = {1:"One",2:"Two",3:"Three"}

# print(mapping)
# print(type((mapping)))


# mapping  = {1:"One",2:"Two",3:"Three"}
# # mapping[4] = 'Four'
# # mapping[5] = 'Five'
# # mapping[4] = 'six'
# # print(mapping)
# mapping.update({3:'Four',5:'Five'})
# print(mapping)

# # hanzala
# # print(desserts['hanzala'])
# print(desserts.get('hanzala','cake'))
# print(desserts.keys())
desserts = {
    'Alice': 'chocolate cake',
    'Bob': 'apple pie',
    'Charlie': 'ice cream',
    'David': 'cheesecake',
    'Emma': 'brownies'
}
# # print(desserts.values())
# # print(desserts.items())
# # print(desserts.pop('David'))
# # print(desserts)
# # a = 10
# # del desserts['David']
# # print(desserts)

# desserts.clear()
# print(desserts)


# capitals = dict(Pakistan='Islamabad',
#                 USA='Washington DC',
#                 Enland='London')
# userInput = input('Enter a country name: ')
# print(capitals.get(userInput,"Sorry, we don't have information about that country."))
# # if userInput in capitals:
# #     print(capitals[userInput])
# # else:
# #     print("Sorry, we don't have information about that country.")
# string = "I love python programming language"
# frequency = {}
# for char in string:
#     char = char.lower()
#     if char in frequency:
#         frequency[char]+=1
#     else:
#         frequency.update({char:1})
# # print(frequency)
# frequency = {'i': 2, ' ': 4, 'l': 2, 'o': 3, 'v': 1, 'e': 2, 'p': 2, 'y': 1, 't': 1, 'h': 1, 'n': 3, 'r': 2, 'g': 4, 'a': 3, 'm': 2, 'u': 1}
# _max = ('',float("-inf"))
# for f in frequency.items():
#     if f[1]>_max[1]:
#         _max = f
# print(_max)
# for f in frequency:
#     if frequency[f]>_max:
#         _max = frequency[f]
# print(_max)


# students  = {
#     'Alice': 89,
#     'Bob': 90,
#     'Charlie': 70,
#     'David': 65,
#     'Emma': 76
# }
# _max = ('',float("-inf"))
# for f in students.items():
#     if f[1]>_max[1]:
#         _max = f
# print(_max)

# order = {'bananas':5,"apples":3,'mangoes':21,'kivy':10}
# market = {'bananas':30,"apples":20,"mangoes":25}
# # total = (fruits.get('bananas')*5) + (fruits.get('apples')*3) + (fruits.get("mangoes")*2)
# total = 0
# for item in order.keys():
#     if item in market:
#         total+=(market[item]*order[item])


# print(f"{total} Rs ")

students = [
    {"name":'Alice',"age":12,"gender":'female'},
    {"name":'Bob',"age":15,"gender":'male'},
    {"name":'Charlie',"age":11,"gender":'male'},
    {"name":'David',"age":13,"gender":'male'},
    {"name":'Emma',"age":16,"gender":'female'},
]

print('Name        Gender        Age')
print('-'*28)
for student in students:
    print(f'{student:<10} {students[student][1]:<14}{students[student][1]:<8}')




