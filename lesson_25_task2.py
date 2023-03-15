class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SiglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):

        if self.head is None:
            new_node = Node(data)
            self.head = new_node


        else:
            new_node = Node(data)
            cur = self.head

            while cur.next:
                cur = cur.next

            new_node.next = None
            cur.next = new_node

    def pop(self):
        if self.head is None:
            raise IndexError

        else:
            cur = self.head

            while cur.next:
                if cur.next.next is None:

                    break
                cur = cur.next

            result = cur.next
            cur.next = None
            return result

    def print(self):
        string = ''
        cur = self.head

        while True:

            if cur.next is None:
                string += str(cur.value)
                break

            string+=str(cur.value)
            cur = cur.next
        print(string)


if __name__ == '__main__':
    stack = SiglyLinkedList()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    x = stack.pop()

    print(x.value)

    stack.print()
