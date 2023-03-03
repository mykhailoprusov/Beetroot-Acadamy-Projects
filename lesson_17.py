import abc
# Task 1

class Animal(abc.ABC):

    @abc.abstractmethod
    def talk(self):
        print('A sound of the animal')

class Cat(Animal):
    def __init__(self):
        pass
    def talk(self):
        print('MEOWWWWWW')

class Dog(Animal):
    def __init__(self):
        pass
    def talk(self):
        print('WOOOOOOOOOOOOFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')

dog1 = Dog()
cat1 = Cat()
animals = [dog1,cat1]

# a = map(lambda x: x.talk(), animals) # чому воно не працює? Ніби норм


def say_hi(self,pets):

    for i in pets:
        i.talk()

Sounds = type('Sounds',(),{'say_hi':say_hi})

s = Sounds()

s.say_hi(animals)

# Task 2

class Library:

    def __init__(self,name):

        self.name = name
        self.books = []
        self.authors = []

    def new_book(self,name,year,author):

        if isinstance(name,str) and isinstance(year,int) and isinstance(author,Author):

            self.books.append(Book(name,year,author))

            return Book(name,year,author)

        raise ValueError('Crap! Change your input otherwise I will not operate')

    def group_by_author(self,author):

        books_by_author = []

        for i in self.books:
            print(i)
            if i.author.name == author:
                books_by_author.append(i)

        return books_by_author if books_by_author else 'No books by such author'

    def group_by_year(self,year):
        books_by_year = []

        for i in self.books:

            if i.year == year:
                books_by_year.append(i)

        return books_by_year if books_by_year else 'Ooops. No books by such year'

    def __repr__(self):

        return repr(f'This is the {self.name} library')

    def __str__(self):

        return f'This is the {self.name} library'

class Book:

    books_number = 0

    def __init__(self,name,year,author):

        self.name= name
        self.year = year
        self.author = author

        Book.books_number+=1

    def __repr__(self):
        return repr(f'{self.name},{self.year},{self.author}')

    def __str__(self):
        return f'{self.name},{self.year},{self.author}'

class Author:

    def __init__(self,name,country,birthday):

        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def add_books(self,*args):

        for i in args:
            self.books.append(i)

    def __repr__(self):
        return repr(f'{self.name},{self.country},{self.birthday}')

    def __str__(self):
        return f'{self.name},{self.country},{self.birthday}'

# Task 3

class Fraction:
    def __init__(self,numerator,denominator):
        if denominator == 0:

            raise ZeroDivisionError('Cannot divide by zero')

        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):

        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):

        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator,denominator)

    def __mul__(self, other):

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator,denominator)

    def __truediv__(self, other):

        if other.denominator == 0:
            raise ZeroDivisionError('Cannot divide by 0')

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator,denominator)

    def simplify(self):

        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def _gcd(a, b):

        if b == 0:
            return a

        else:
            return Fraction._gcd(b, a % b)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

if __name__ == '__main__':

    lib1 = Library('Glasgow')
    lib1.new_book('lalla',2020,Author('Mike','Ukraine',2005))

    lib1.new_book('Foo',2017,Author('Mike','Ukraine',2005))
    lib1.new_book('Poo',2015,Author('Mike','Ukraine',2005))
    lib1.new_book('Poo',2014,Author('Gandalf','UK',2000))

    x = lib1.group_by_author('Mike')
    print(x)

    x = Fraction(1, 2)
    y = Fraction(1, 4)

    z = x + y
    z1 = x - y
    z2 = x * y
    z3 = x / y

    z.simplify()
    z1.simplify()
    z2.simplify()
    z3.simplify()

    # print(z)
    # print(z1)
    # print(z2)
    # print(z3)

    assert x + y == Fraction(3,4)
    assert x - y == Fraction(1,4)
    assert x * y == Fraction(1,8)
    assert x / y == Fraction(2,1)
