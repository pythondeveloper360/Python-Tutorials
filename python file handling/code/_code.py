# file = open('textz.txt')
# print(file.read())
# file.close()

# file = open('text.txt',mode = 'w')
# lines = ['Python is awesome\n','Python is easy\n']
# file.writelines(lines)
# file.close()
# file = open('random.txt','x')
# file.write('Random')
# file.close()

# file = open('text copy.txt','a')
# file.write('\nPython is easy')
# file.close()
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# lines = file.readlines()
# for line in lines:
#     print(line)
# # string.split('\n')
# file = open('text copy.txt','r')
# file.write('Python')


# n = int(input('Enter the Number: '))

# file = open('squares.txt','w')

# for i in range(1,n+1):
#     square = i**2
#     file.write(f'{i}**2 = {square}\n')
# file.close()
# numbersFile = open('numbers.txt','r')
# oddFile = open('odd.txt','w')
# evenFile = open('even.txt','w')
# primeFile = open('prime.txt','w')
# oddList = []
# evenList = []
# primeList = []
# def prime(n):
#     for i in range(2,n):
#         if n%i ==0 :
#             return False
#     return True


# def even(n):
#     if n%2 ==0:
#         return True
#     return False

# numbers = numbersFile.read().split(',')
# for number in numbers:
#     number = int(number)
#     if prime(number):
#         primeList.append(f'{number}\n')
#     if even(number):
#         evenList.append(f"{number}\n")
#     else:
#         oddList.append(f"{number}\n")
# # print(oddList)

# oddFile.writelines(oddList)
# evenFile.writelines(evenList)
# primeFile.writelines(primeList)


# primeFile.close()
# evenFile.close()
# oddFile.close()
# numbersFile.close()

# fruitsFile = open('fruits.txt','r')
# fruits = fruitsFile.read().split('\n')
# count = {}
# for fruit in fruits:
#     if count.get(fruit):
#         count[fruit]+=1
#     else:
#         count.update({fruit:1})
# print(count)
# detailsFile = open('details.txt','r')
# detailsList = detailsFile.read().split('\n')


# book = []
# for d in detailsList:
#     details = d.split(',')
#     book.append({'name':details[0].replace('\n',''),'Street':details[1],
#                  'City':details[2],"age":details[3]})
# print(book)
accountsFile = open('accounts.txt','r')
accountList = accountsFile.read().split('\n')
database = {}

for account in accountList:
    account = account.split(',')
    database.update({account[1].replace(" ",''):[account[0],account[2].replace(' ','')]})

def auth(username,password):
    if username in database:
        details = database.get(username)
        if details[1] == password:
            print(f'Welcome {details[0]}')
            return 
        else:
            print("Incorrect Password")
            return
    print('Username not found')
    return




