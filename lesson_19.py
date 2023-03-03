# Task 1
class With_index:
    def __init__(self,iterable,start=-1):
        self.iterable = iterable
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        self.start+=1
        return (self.start,self.iterable[self.start])

# Task 2
def in_range(start,end,step=1):

    while start < end:
        yield start
        start+=step


# Task 3
class SchoolClass:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.current = 0

    def __iter__(self):
        return self

    @property
    def end(self):
        return len(self.students)

    def __next__(self):
        if self.current >= self.end:
            self.current = 0
            raise StopIteration
        else:
            index = self.current
            self.current +=1
            return self.students[index]


    def __getitem__(self, index):
        return self.students[index]

    def add_student(self,new_student):
        self.students.append(new_student)

    def __str__(self):
        return str(self.name)

class Student:
    def __init__(self,name:str, *marks):
        self.name = name
        self.marks = list(marks)

    def __str__(self):
        return f'Name: {self.name}, Marks: {self.marks}'


if __name__ == '__main__':
    # x = With_index([1,2,3,4,5])
    # print(next(x))
    # print(next(x))
    #
    # x = in_range(1,10)
    # for i in x:
    #     print(i)

    st1 = Student('Mykhailo Prusov',7,10,5,9,8)
    st2 = Student('Geldalf',4,2,2,1,7,5)

    cl1 = SchoolClass('Class 10-B')
    cl1.add_student(st1)
    cl1.add_student(st2)

    for i in cl1:
        print(i)

    # assert str(cl1[0]) == 'Mykhailo Prusov, Marks: [7, 10, 5, 9, 8]' чому воно так не спрацює?