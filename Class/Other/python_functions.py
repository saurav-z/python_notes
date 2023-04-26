# #Function to add 2 numbers

# def get_month_name(month):
#     if month == 1:
#         return "January"
#     elif month ==2:
#         return "Feb"
#     elif month == 3:
#         return "March"
#     elif month == 4:
#         return "April"
#     elif month == 5:
#         return "May"
#     elif month == 6:
#         return "June"
#     elif month == 7:
#         return "July"
#     elif month == 8:
#         return "August"
#     elif month == 9:
#         return "September"
#     elif month == 10:
#         return "October"
#     elif month == 11:
#         return "November"
#     elif month == 12:
#         return "December"
#     else:
#         return "Invalid"

# month = int(input("Enter a month number:"))
# print(get_month_name(month))

#Types of user-defined function.
# 1. Function with return type and argument.
# 2. Function with return type and no argument.
# 3.Function with no return type and argument.
# 4.Function with no return type and no argument.

# def PrintHello():
#     print("Evol World")

# PrintHello()
# PrintHello()

# def AddTwoNumber(a,b):
#     print(f"The sum of {a} and {b} is {a+b}")

# AddTwoNumber(3,4)

# def AddTwoNumber():
#     a = int(input("Enter a value for a:"))
#     b = int(input("Enter a value for b:"))
#     return a+b

# print(AddTwoNumber())

# import math
# #Sqrt computes the square root
# square_root = math.sqrt(4)
# print("Square root of 4 is ", square_root)
# #pow() computes the power
# power = pow(2,3)
# print("2 to the power 3 is ", power)

# def my_programming(*args):
#     print("My best programming lang is "+ args)

# my_programming("C", "Python", "Javascript")

# def my_subjects(**subject):
#     print("My fav sub is " + subject['first'])

# my_subjects(first = "Science", second = "Computer", third = "Nepali")


# def add(x,y):
#     print(x+y)

# add(2,3)

# # Positional Arguments
# def info(Name,Class,Roll_no):
#     print(f'Hello {Name} You Study in class {Class} and your Roll No is {Roll_no}')

# info('Neshan',11,24024)

# # Positionless Argument
# def info(Name,Class,Roll_no):
#     print(f'Hello {Name} You Study in class {Class} and your Roll No is {Roll_no}')

# info(Name='Neshan',Class=11,Roll_no=24024)




# #Default Argument
# def balance(balance=1):
#      print(f'Your balance is {balance}')
# balance(balance=10)

# #This can add as many numbers as input.
# def add(*args):
#     total=0
#     for i in args:
#         total=total+i
#     print(total)


# add(1,2,3)

# # Multiple keywords input
# def keyarg(**kwargs):
#     print(kwargs)
  

# keyarg(fn='Neshan')
# keyarg(fn='Neshan',ln='Hacke')


# def add(i,j):
#     return i+j
# print(add(2,3))

# def mean(*args):
#     sum=0
#     length=len(args)
#     for i in args:
#         sum=sum+i
    
#     return sum/length
        
        
# print(mean(10,20,30,40,50))

def multiply(*args):
    multi=1
    for item in args:
        multi=multi*item
    return multi
print(multiply(2,5,3,3,4,5))
