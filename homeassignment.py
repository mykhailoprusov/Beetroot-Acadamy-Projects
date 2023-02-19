import random

comp_num = random.randint(1,10)
user_num = int(input('Type one number ranging from 1 to 10 '))

if user_num == comp_num:
    print('Correct!!')

else:
    print('You lost')

# Task 2

name = input('Write your name here ')
age = int(input('Write your age here '))

print('Hello %s, on your next birthday you will be %d years' % (name,age+1))

# Task 3

string = input('Enter any string ')

randomized = ''.join(random.sample(string,k=len(string)))
randomized2 = ''.join(random.sample(string,k=len(string)))
randomized3 = ''.join(random.sample(string,k=len(string)))
randomized4 = ''.join(random.sample(string,k=len(string)))
randomized5 = ''.join(random.sample(string,k=len(string)))

print(randomized)
print(randomized2)
print(randomized3)
print(randomized4)
print(randomized5)

print('fixed')