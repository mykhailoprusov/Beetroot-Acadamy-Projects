# Я вирішив просто створити звичайне дерево

class Tree:
    def __init__(self,data):
        self.children = []
        self.parent = None
        self.data = data

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        ancestor = self.parent
        while ancestor:
            level +=1
            ancestor = ancestor.parent
        return level

    def get_prefix(self,level):
        space = ' ' * level * 4
        return space + '___' if self.parent else space

    def print_tree(self):
        position = self.get_level()
        beginning = self.get_prefix(position)

        print(beginning + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

if __name__ == '__main__':

    root = Tree('Chairman')

    ceo = Tree('CEO')

    manager1 = Tree('Finance Manager')
    manager2 = Tree('Technology Manager')
    manager3 = Tree('Marketing Manager')
    manager4 = Tree('Legal Manager')

    clerk1 = Tree('Clerk')
    clerk2 = Tree('Clerk')
    clerk3 = Tree('Clerk')
    clerk4 = Tree('Clerk')
    clerk5 = Tree('Clerk')
    clerk6 = Tree('Clerk')
    clerk7 = Tree('Clerk')
    clerk8 = Tree('Clerk')
    clerk9 = Tree('Clerk')
    clerk10 = Tree('Clerk')
    clerk11 = Tree('Clerk')
    clerk12 = Tree('Clerk')

    root.add_child(ceo)

    ceo.add_child(manager1)
    ceo.add_child(manager2)
    ceo.add_child(manager3)
    ceo.add_child(manager4)

    manager1.add_child(clerk1)
    manager1.add_child(clerk2)
    manager1.add_child(clerk3)

    manager2.add_child(clerk4)
    manager2.add_child(clerk5)
    manager2.add_child(clerk6)

    manager3.add_child(clerk7)
    manager3.add_child(clerk8)
    manager3.add_child(clerk9)

    manager4.add_child(clerk10)
    manager4.add_child(clerk11)
    manager4.add_child(clerk12)

    root.print_tree()


