# capitals = dict(Pakistan = 'Islamabad',
#                 USA = 'Washington DC',
#                 Enland = "London")
# print(capitals)

# # mapping = {1:"ONE",2:"TWO",3:"THREE"}
# # print(type(mapping))
# # print(mapping)

# # capitals = dict(Pakistan = 'Islamabad',
# #                 USA = 'Washington DC',
# #                 Enland = "London")
# # capitals['India'] = 'New Dehli'
# # print(capitals)
# # functions
# # capitals.update({'India':'New Dehli'})
# # print(capitals)

# # desserts = {
# #     'Alice': 'chocolate cake',
# #     'Bob': 'apple pie',
# #     'Charlie': 'ice cream',
# #     'David': 'cheesecake',
# #     'Emma': 'brownies'
# # }

# # # print(desserts['Hanzala'])

# # desserts = {
# #     'Alice': 'chocolate cake',
# #     'Bob': 'apple pie',
# #     'Ch   arlie': 'ice cream',
# #     'David': 'cheesecake',
# #     'Emma': 'brownies'
# # }
# # # print(desserts.keys())
# # # print(desserts.values())
# # # print(desserts.items())

# # # cancelItem = desserts.pop('Alice')
# # # print(cancelItem)
# # # del desserts['Alice']
# # # print(desserts)
# # desserts.clear()
# # print(desserts)

# # capitals = dict(Pakistan = 'Islamabad',
# #                 USA = 'Washington DC',
# #                 Enland = "London")
# # userInput = input('Enter Country Name: ')
# # print(capitals.get(userInput, "Sorry, we don't have information about that country."))

# # string = "I love python programming language"
# # count = {}
# # for char in string:
# #     char = char.lower()
# #     if char in count:
# #         count[char]+=1
# #     else:
# #         count.update({char:1})


# # _max = ('' ,float("-inf"))
# # for i in count.items():
# #     if i[1]> _max[1]:
# #         _max = i
# # print(_max)


# # Grades = {
# #     'Alice': 90,
# #     'Bob': 87,
# #     'Charlie': 70,
# #     'David': 91,
# #     'Emma': 94
# # }


# # _max = ('' ,float("-inf"))
# # for i in Grades.items():
# #     if i[1]> _max[1]:
# #         _max = i
# # print(_max)


# # market = {'Bananas':20,'Mangoes':30,'Apples':25}
# # order = {'Bananas':5,'Mangoes':2,'Apples':3,'kivy':12}

# # total = 0
# # for item in order.keys():
# #     if item in market:
# #         total+= market.get(item)*order.get(item)
# # print(total)

# # 235

# students = [
#     {"name":'Alice',"age":12,"gender":'female'},
#     {"name":'Bob',"age":15,"gender":'male'},
#     {"name":'Charlie',"age":11,"gender":'male'},
#     {"name":'David',"age":13,"gender":'male'},
#     {"name":'Emma',"age":16,"gender":'female'},
# ]
# print('Name       Age       Gender')
# print('-'*27)
# for student in students:
#     print(f'{student.get("name"):<10} {student.get("age"):<10} {student.get("gender"):<9}')