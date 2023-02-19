# Task 1

def favourite_movie(movie):
    print('My favourite movie is named %s'% (movie))

favourite_movie('Peaceful warrior')
# Task 2

def make_country(name,capital):
    dic = {}
    dic[name] = capital

    print(dic)

make_country('Ukraine','Kyiv')

# Task 3

def make_operation(operator,*args):

    if operator == '+':
        return sum(args)

    elif operator == '-':
        subtract = 0

        for i,j in enumerate(args): # максимально тупий спосіб,але щось нічого кращого не спало на думку ((

            if i == 0:
                subtract+=j

            else:
                subtract = subtract + (-j)
        return subtract

    elif operator == '*':
        multiplication = 1

        for i in args:
            multiplication*=i
        return multiplication

    else:
        return 'Unsupported operator'

result = make_operation('-',2,2)
print(result)