# Task 1
class Email:

    def __init__(self,email):
        self.email = self.validate(email)

    @staticmethod
    def validate(item):
        valid_endings = ['mail.com', 'mail.cc', 'mail-archive.com', 'mail.org']

        split_item = item.split('@')
        part1,part2 = split_item

        if part1[0] == '.' or part1[-1] == '.' or part1[-1] == '-' or '#' in part1:

            raise ValueError('Invalid format of the email')

        elif part2 not in valid_endings:

            raise ValueError('Invalid format of the email')
        return item

# Task 2
class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self._workers = [] # я правильно розумію, що у цьому випадку ми можемо працювати
        # тільки через приватні змінні?

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self,args):
        # new_workers = [x for x in args if x is Worker]
        self._workers = self._workers + list(args)

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company

        self._boss = None

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self,new_boss):
        if isinstance(new_boss,Boss):
            self._boss = new_boss
        raise ValueError()

class TypeDecorators:
    def __init__(self,orig_func):
        self.orig_func = orig_func

    def __call__(self,x,do):
        if isinstance(x,str) and do == 'to_int':
            new_value = int(x)
            result = self.orig_func(new_value)
            return result
        elif isinstance(x,str) and do == 'to_bool':
            new_value = bool(x)
            result = self.orig_func(new_value)
            return result
        elif isinstance(x,int) and do == 'to_float':
            new_value = float(x)
            result = self.orig_func(new_value)
            return result

@TypeDecorators
def do_nothing(string: str):
    return string

@TypeDecorators
def do_something(string:str):
    return string

if __name__ == '__main__':

    letter1 = Email('abc.def@mail-archive.com')
    # letter2 = Email('.abc@mail.com')
    # letter2 = Email('abc-@mail.com')
    # assert Email('abc.def@mail-archive.com') == а якось можна це перевірити за допомогою assert?

    b1 = Boss(12435737,'Mykhailo Prusov','Tesla')

    w1 = Worker(66327062,'Nik Otaman','Tesla',b1)
    w2 = Worker(66327833,'Jack Borsh','Tesla',b1)
    w3 = Worker(66327901,'Gandalf Kozak','Tesla',b1)

    b1.workers = w1,w2,w3
    print(b1.workers)


    # print(do_nothing('25','to_int'))
    # print(do_something('25','to_bool'))
    # print(do_something(12,'to_float'))
