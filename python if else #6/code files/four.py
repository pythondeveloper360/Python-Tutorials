# name = 'hanzala'

# username = input('Enter your name : ')

# print()

# num1 = 10

# num2 = 29

# num3 = 30 

# print(num1<num2<num3)
# name = 'hanzala'
# username = input('Enter your name: ')

# print(name == username)

# age = float(input('Enter your age: '))

# print(1<age<=16)


# name = 'hanzala'
# username = input('Enter your name: ')

# print(id(name))
# print(id(username))
# # print(name is name)

# superuser = 'hanzala'
# user = 'hamza'
# username = input('Enter your name: ')

# if superuser == username:
#     print('its your computer you are admin')
# elif user == username:
#     print('you can log in')
# else:
#     print('its not your computer')


# score = float(input('Enter your grades: '))
# grade = ''

# if score >=90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >=70:
#     grade = 'C'
# elif score >=60:
#     grade = 'D'
# else:
#     grade = 'F'
# print(grade)

year = int(input("Enter the year: "))
leapyear = False

if year%4==0:
    leapyear = True
    if year %400 == 0:
        print('400')
        leapyear = True
    elif year % 100 !=0:
        leapyear = False
    else:
        leapyear = False
print(leapyear)







