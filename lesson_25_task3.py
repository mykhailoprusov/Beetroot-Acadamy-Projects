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

    def pop(self):
        if self.head is None:
            raise IndexError

        elif self.head.next is None:
            cur = self.head
            self.head = None
            return cur

        else:
            cur = self.head
            self.head = self.head.next
            return cur

if __name__ == '__main__':
    queue = SiglyLinkedList()

    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)

    queue.pop()

    queue.print()






