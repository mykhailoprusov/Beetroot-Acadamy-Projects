class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):

        if self.head is None:
            new_node = Node(value)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = Node(value)
            cur = self.head

            while cur.next:
                cur = cur.next

            new_node.prev = cur
            new_node.next = None

            cur.next = new_node

    def pop(self):

        if self.head is None:
            raise IndexError('pop from empty DoublyLinkedList')

        else:
            cur = self.head
            while cur.next:
                cur = cur.next

            cur_prev = cur.prev
            cur_prev.next = None

    def index(self,value):
        if self.head is None:
            raise IndexError('There are no elements in the list')
        else:
            position = -1
            cur = self.head

            while True:
                if cur.data == value:
                    position+=1
                    break

                elif cur.next is None:
                    position = None
                    break

                else:
                    position+=1
                    cur = cur.next

            return position

    def insert(self,position,value):

        new_node = Node(value)
        cur = self.head
        index = 0

        while True:
            if index == position:

                prev_ = cur.prev
                prev_.next = new_node
                new_node.next = cur
                cur.prev = new_node
                break

            elif cur.next is None:
                break

            else:
                index+=1
                cur = cur.next

if __name__ == '__main__':
    unordered_list = DoublyLinkedList()

    unordered_list.append('Mykhailo')
    unordered_list.append('Gendalf')


    print(unordered_list.index('Gendalf'))

    unordered_list.insert(1,'Frodo')

    print(unordered_list.index('Gendalf'))

    unordered_list.pop()

    print(unordered_list.index('Gendalf'))