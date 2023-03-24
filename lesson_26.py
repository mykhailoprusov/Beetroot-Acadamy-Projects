# Task 1
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self,current,value):
        if self.root is None:
            self.root = Node(value)

        else:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                else:
                    self.add(current.left,value)
            else:
                if current.right is None:
                    current.right = Node(value)
                else:
                    self.add(current.right,value)










# Task 2
def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)


def FibonacciSearch(arr, x):
    m = 0
    while FibonacciGenerator(m) < len(arr): #
        m = m + 1
    offset = -1
    while (FibonacciGenerator(m) > 1):
        i = min( offset + FibonacciGenerator(m - 2) , len(arr) - 1)
        print('Current Element : ',arr[i])
        if (x > arr[i]):
            m = m - 1
            offset = i
        elif (x < arr[i]):
            m = m - 2
        else:
            return i
    if(FibonacciGenerator(m - 1) and arr[offset + 1] == x):
        return offset + 1
    return -1

if __name__ == '__main__':

    arr = [12,20,34,37,79,90,100,103,145]
    x = 90
    print('Number found at index : ',FibonacciSearch(arr, x))