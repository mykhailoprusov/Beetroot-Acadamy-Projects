# Task 1
def oops():
    raise IndexError

def oops2():

    try:
        oops()

    except IndexError: # if I change raise IndexError to raise KeyError then I my program will crash
        print('Gotcha!')

oops2()

# Task 2

a = input('Give me first number ')
b = input('Give me second number ')

def calculations(a,b):

    try:
        a = int(a)
        b = int(b)
        new_num = pow(a,2)/b
        return new_num

    except ValueError:
        print('The given number was not a decimal one')

    except ZeroDivisionError:
        print('Drill your math! You cannot divide by 0!!!')

result = calculations(a,b)
print(result)