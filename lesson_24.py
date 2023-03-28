# Task 1
from queue import LifoQueue
from queue import Queue
from collections import deque

stack = LifoQueue()

stack.put('I ADORE OOP!')
stack.put('SOS')
stack.put(1234)
stack.put([1,2,3])
stack.put(1.00)
stack.put(True)

for i in range(stack.qsize()):
    print(stack.get())


# Task 2

#((( )))
# ))) (((
#())(

def balanced_string(word):

    stack_2 = LifoQueue()

    for i in word:
        if i == '(':
            stack_2.put(i)
        elif i == ')':
            if stack_2.qsize() > 0:
                bracket = stack_2.get()
                if bracket != '(':
                    return None
            else:
                return None

    if stack_2.qsize() >0:
        return None
    return True
# Task 3


class Stack:
    def __init__(self):
        self._data = []

    def push(self,value):
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def get_from_stack(self,value):
        try:
            self._data.remove(value)
            return value
        except ValueError:
            raise ValueError('Value is not in Stack')


class MyQueue:
    def __init__(self):
        self._data = []

    def push(self,value):
        self._data.append(value)

    def pop(self):
        return self._data.pop(0)

    def get_from_queue(self,value):
        try:
            self._data.remove(value)
            return value
        except ValueError:
            raise ValueError('Value is not in Queue')


if __name__ == '__main__':

    # stack_1 = Stack()
    #
    # stack_1.push(222)
    # x = stack_1.pop()
    #
    # print(x)
    #
    # stack_1.get_from_stack('a')

    assert balanced_string('(abc)()()((())()') == None

