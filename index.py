# def sum(a,b):
#     return a + b

# print(sum(20,20))

# -------------------------------------------

# sumLambda = lambda a, b: a + b

# print(sumLambda(2,3))

# -------------------------------------------

# def calcSquare(lsit):
#     newList = []
#     for num in list:
#         newList.append(num * num)
#     return newList

# print(calcSquare([1, 2, 3, 4, 5]))

# --------------------------------------------

# calcSquraes = lambda list: [num * num for num in list ]

# print(calcSquraes([1, 2, 3, 4, 5 ]))

# sum = lambda num1: lambda num2: num1 + num2

# print(sum(2)(3))

# ---------------------------------------------

# def upper(txt):
#     return txt.upper()
    
# def lower(txt):
#     return txt.lower()

# def say_hello(func: str):
#     greeting = func('Hello! I am Elbek')
#     print(greeting)

# print(upper('Hello'))
# print(lower('PHP'))
# say_hello(upper)
# say_hello(lower)

# ----------------------------------------------

# def say_hello(type, txt):
#     if type == 'upper':
#         print(txt.upper())
#     else:print(txt.lower())

# say_hello('lower', 'Elbek')

# -----------------------------------------------

# string = 'Hello I am elbek'
# urlFriendly = []

# for char in string :
#     if char == ' ':
#         urlFriendly.append('_')
#     else: urlFriendly.append(char)

# urlFriendly = ''.join(urlFriendly)
# print(urlFriendly)

# ------------------------------------------------

# string2 = 'Hello I am Elbek'
# urlFriendly2 = string2.replace(' ', '_')
# print(urlFriendly2)

# ------------------------------------------------

# def calcLoan(credit, period, interst):
#     total = credit + credit * (interst/100) * period
#     perMonth = total / (period * 12)
#     perMonthSums = perMonth * 10800
#     return f'You have to pay {int(perMonthSums)} sums per month'


# print(calcLoan(1000, 3, 26))