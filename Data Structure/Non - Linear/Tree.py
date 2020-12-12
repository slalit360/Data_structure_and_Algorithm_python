# Data Structure	                                    Time Complexity
#                       Average	                                            Worst
#                       Access	    Search	    Insertion	Deletion	    Access	Search	Insertion	Deletion
# Binary Search Tree	Θ(log(n))	Θ(log(n))	Θ(log(n))	Θ(log(n))	    O(n)	O(n)	O(n)	    O(n)

# General Tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def print_tree(self):
        lvl = self.get_level()
        if lvl == 0:
            print(self.data)
        else:
            print("\t" * lvl + "|__", self.data)

        # if self.child:
        for child in self.child:
            child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


if __name__ == '__main__':
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Apple'))
    laptop.add_child(TreeNode('Dell'))
    laptop.add_child(TreeNode('Hp'))

    cell = TreeNode('Cellphone')
    cell.add_child(TreeNode('Iphone'))
    cell.add_child(TreeNode('Pixel'))
    cell.add_child(TreeNode('Samsung'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('OnePlus'))

    root.add_child(laptop)
    root.add_child(cell)
    root.add_child(tv)

    root.print_tree()
    print("\n")


# exercise
class CompanyTreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def print_tree(self, type=None, level=None):
        if level is not None:
            if self.get_level() > level:
                return

        if type == 'both' or type is None:
            value = self.name + " (" + self.designation + ")"
        else:
            value = self.__dict__[type]

        prefix_format = "\t" * self.get_level() + "|__" if self.parent else ""
        print(prefix_format + str(value))

        if self.child:
            for child in self.child:
                child.print_tree(type, level)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


if __name__ == '__main__':
    ceo = CompanyTreeNode('Nilupul', 'CEO')

    cto = CompanyTreeNode('Chinmay', 'CTO')
    ifhead = CompanyTreeNode('Vishva', 'Infrastructure HEAD')
    ifhead.add_child(CompanyTreeNode('Dhaval', 'Cloud manager'))
    ifhead.add_child(CompanyTreeNode('Abhijit', 'App manager'))
    apphead = CompanyTreeNode('Aamir', 'Application HEAD')
    cto.add_child(ifhead)
    cto.add_child(apphead)

    hr = CompanyTreeNode('Gels', 'HR HEAD')
    hr.add_child(CompanyTreeNode('Peter', 'Recruitment manager'))
    hr.add_child(CompanyTreeNode('Waqas', 'Policy manager'))

    ceo.add_child(cto)
    ceo.add_child(hr)

    ceo.print_tree(type='name')
    print("\n")
    ceo.print_tree(type='designation')
    print("\n")
    ceo.print_tree()
    print("\n")
    ceo.print_tree(level=2, type='both')
    print("\n")
