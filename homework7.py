# Task 1
string = 'I am not responsible for this code and I was forsed to write it against my will'
words = string.split()
set_ = set(words)
data = {}

for i in set_:
    counter = string.count(i)
    data[i] = counter

print(data)
# Task 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_stock = [stock[x] for x in stock]
total_price = [prices[y] for y in prices]
total = [total_price[i]*total_stock[i] for i in range(len(total_price))]

print('The sum is',sum(total))

# Task 3

answer = [(i,i**2) for i in range(1,11)]
print(answer)

# Task 4

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
days1 = {days.index(i)+1: i for i in days}
days2 = {i : days.index(i)+1 for i in days} # Тепер я знаю наскільки comprehension круте

print(days1)
print(days2)