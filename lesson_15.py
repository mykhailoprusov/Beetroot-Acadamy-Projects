# Task1
class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I am {self.age} years old')

person1 = Person('Mykhailo','Prusov','17')
person1.talk()

# Task 2

class Dog():
    age_factor = 7
    def __init__(self,age):
        self.age = age
    def human_age(self):
        return self.age * self.age_factor
dog1 = Dog(5)
print(dog1.human_age())
# Task 3
class TVController:

    def __init__(self,channels):
        self.channels = channels
        self.current_channel_ = channels[0] # чомусь,якщо замінити channels[0] на
        #self.channels[0], функція next_channel перестане працювати правильно
    def first_channel(self):
        self.current_channel_ = self.channels[0]
        print(self.current_channel_)
    def second_channel(self):
        self.current_channel_ = self.channels[1]
        print(self.current_channel_)
    def next_channel(self):
        self.index = self.channels.index(self.current_channel_)
        self.current_channel_ = self.channels[self.index + 1]
        print(self.current_channel_)
    def previous_channel(self):
        self.index = self.channels.index(self.current_channel_) #чи можна змінну self.index
        # оголосити просто index, чи так не можна?
        self.current_channel_ = self.channels[self.index-1]
        print(self.current_channel_)
    def current_channel(self):
        print(self.current_channel_)
    def is_exist(self,name):
        self.name = name
        if isinstance(self.name,int):
            try:
                print(f'There is a {self.channels[name-1]} channel')
            except:
                print('No such channel')
        elif self.name.isalpha():
            try:
                index = self.channels.index(self.name)
                print(f'There is a {self.channels[index]} channel')
            except:
                print('No such channel')
        else:
            print('Invalid input')
CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

controller.next_channel()
controller.next_channel()
controller.previous_channel()
controller.is_exist('BBC')
controller.is_exist([1,2,3]) # чомусь не працює