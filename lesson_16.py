import logging
# task 1
class Person(object):
    def __init__(self,firstname,surname,age,skin_colour,nationality,hair_colour,sex):

        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.skin_colour = skin_colour
        self.nationality = nationality
        self.hair_colour = hair_colour
        self.sex = sex


    def get_name(self):
        return f'My name is {self.firstname} {self.surname}'

    def get_info(self):
        return f'Name: {self.firstname} {self.surname}, age: {self.age} , skin colour: {self.skin_colour}' \
               f'nationality: {self.nationality}, hair colour: {self.hair_colour}, sex: {self.sex} '

class Teacher(Person):
    def __init__(self,firstname,surname,age,skin_colour,nationality,hair_colour,sex,salary,subject):
        super().__init__(firstname,surname,age,skin_colour,nationality,hair_colour,sex)

        self.salary = salary
        self.subject = subject
        self.classes = []

    def check_assignment(self):
        print('**staring at the work**')
        print('What a piece of .... ')

    def get_salary(self):
        return self.salary

    def add_class(self,new_class):
        self.classes = self.classes.append(new_class)

    def my_subject(self):
        print(f'I teach {self.subject}')

class Student(Person):
    def __init__(self,firstname,surname,age,skin_colour,nationality,hair_colour,sex,grade,school):
        super().__init__(firstname,surname,age,skin_colour,nationality,hair_colour,sex)

        self.grade = grade
        self.school = school
        self.girlfriend_boyfriend = False

    def get_relationships(self):
        return self.girlfriend_boyfriend
    def change_reletionships(self):
        self.girlfriend_boyfriend = True if self.girlfriend_boyfriend == False else False

    def get_grade(self):
        return self.grade

    def get_school(self):
        return self.school

# Task 2

def positive_nums(x):
    if x < 0:
        return x

def remove_leap(x):
    if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
        return x


class Mathematician:

    @staticmethod
    def square_nums(lst):
        new_lst = list(map(lambda x: x**2,lst))
        return new_lst
    @staticmethod
    def remove_positives(lst):
        new_lst = list(filter(positive_nums,lst))
        return new_lst

    @staticmethod
    def filter_leaps(lst):
        new_lst = list(filter(remove_leap,lst))
        return new_lst

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

# Task 3

class Product:
    def __init__(self,type_,name,price):
        self.type_ = type_
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.price)

class ProductStore:
    income = 0
    def __init__(self):
        self.storage = []

    def add(self,product,amount):
        self.storage.append([product,amount])
        print('You have successfully added item to the storage!')

    def set_discount(self,discount,*args):
        print(args)
        discounted = []

        for i in self.storage:

            for j in args:

                if i[0].name == j:

                    i[0].price = (i[0].price *(100-discount))/100
                    discounted.append([i[0],i[1]])

                else:
                    discounted.append(i)
        self.storage = discounted

    def sell_product(self,product_name,amount):

        for i in self.storage:

            if i[0].name == product_name:

                i[1] = i[1] - amount
                self.income += amount * i[0].price

    def get_income(self):
        return self.income

    def get_all_products(self):
        for i in self.storage:
            print(f'There are >>> {i[0].name}')

    def get_product_info(self,merch):
        for i in self.storage:
            if i[0].name == merch :
                return (i[0].name,i[1])



apple = Product('Food', 'Apples', 70)
orrange = Product('Food','Orranges',50)

b = ProductStore()
b.add(apple,100)
b.add(orrange,200)
b.set_discount(20,'Apples','Orranges')
print(b.storage) # Я і гадки не маю,чому воно додає кожного продукту по два... Я вже так задовбався з цією
# програмою. Ненавиджу її. Я не можу знайти помилку..........................

b.sell_product('Apples',5)
print(b.storage[0][1])
print(b.income)
print(b.storage)
print(b.get_product_info('Orranges'))

# Task 4

logging.basicConfig(filename='logs.log',level=logging.INFO)

class CustomException(Exception):
    def __init__(self,msg):
        self.msg = msg
        logging.info(self.msg)

raise CustomException('Go study math problem')
