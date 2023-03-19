from json import dumps, loads
from random import shuffle
# data = '{ "name":"John", "age":30, "city":"New York"}'

# # _data = json.loads(data)

# # print(_data['name'])
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# _data = json.dumps(x)
# print(_data)

alpha = [
    *[chr(i) for i in range(ord("a"), ord("z")+1)],
    *[chr(i) for i in range(ord("A"), ord("Z")+1)],
    *[str(i) for i in range(0, 10)],
]
# characters,numbers,alpha,ALPHA


def generatePassword(_range=10):
    shuffle(alpha)
    return ''.join(alpha[:_range])


def storePassword():
    website = input("Enter Website name: ")
    password = input("Enter Password(blank generated): ")
    file = open('password.json', 'r')
    data = loads(file.read())
    data['password'].update(
        {website: password if password else generatePassword()})
    file.close()
    fileWrite = open('password.json', 'w')
    fileWrite.write(dumps(data))
    fileWrite.close()


def getPassword():
    website = input("Enter Website name: ")
    file = open('password.json', 'r')
    data = loads(file.read())
    file.close()
    password = data['password'].get(website)
    print(password) if password else print('Password Not Found')


optionsMap = {
    '1': storePassword,
    "2": getPassword,
    "3": storePassword

}
options = """
1) Store Password
2) Retrieve Password
3) Update Password
any key) Quit
"""


print(options)

while True:
    userInput = input("Enter Option: ")
    if userInput in optionsMap:
        optionsMap.get(userInput)()
    else:
        break
