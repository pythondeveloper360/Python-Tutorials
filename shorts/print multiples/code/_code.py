numbers = [i for i in range(1, 23)]
"""
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21

"""
MaxPerline = 5


previous = 0

_next = previous+MaxPerline

for i in range(len(numbers)//MaxPerline):

    print(*numbers[previous:_next])

    previous, _next = _next, _next+MaxPerline

print(*numbers[previous:])
