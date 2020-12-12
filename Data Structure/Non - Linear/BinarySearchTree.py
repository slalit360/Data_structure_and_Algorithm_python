# Data Structure	                                    Time Complexity
#                       Average	                                            Worst
#                       Access	    Search	    Insertion	Deletion	    Access	Search	Insertion	Deletion
# Binary Search Tree	Θ(log(n))	Θ(log(n))	Θ(log(n))	Θ(log(n))	    O(n)	O(n)	O(n)	    O(n)

# BST node can have at-most 2 nodes / child
# node get stores based on value of node, smaller on left node and higher on right node

# Binary Tree searching methods (recursive technique):-
# 1. Breadth first search

# 2. depth first search/ traversal: (D - root, L - Left, R - Right)
#   2.1 Preorder traversal  [D-L-R]
#   2.2 Inorder traversal   [L-D-R]
#   2.3 Postorder traversal [L-R-D]

# can be used for sorting unique values ( no duplicate allowed )
# best case for storing set values

# BinarySearchTreeNode
class BSTNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def insert_node(self, data):

        if data < self.data:
            # add node in left sub tree
            if self.left:
                self.left.insert_node(data=data)
            else:
                self.left = BSTNode(value=data)
        elif data > self.data:
            # add node in right sub tree
            if self.right:
                self.right.insert_node(data=data)
            else:
                self.right = BSTNode(value=data)
        elif self.data == data:
            return

    def delete_node(self, value):
        # 3 delete cases :
        # 1.    delete node with zero child
        # 2.    delete node with one child
        # 3.    delete node with two child
        if value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)
        # exact node to be deleted
        else:
            # ( with zero element)
            # return None (de link) to delete leaf node
            if self.left is None and self.right is None:
                return None
            # ( with one element)
            # return right (de link left or link right) to delete leaf node
            if self.left is None:
                return self.right
            # ( with one element)
            # return left (de link right or link left) to delete leaf node ( with one element)
            if self.right is None:
                return self.left

            # ( having both node)
            # approach one
            min_val = self.right.find_min()     # find min from right sub tree
            self.data = min_val                 # replace min with self data
            self.right = self.right.delete_node(min_val)    # remove min from right sub tree recursively

            # ( having both node)
            # approach two
            # max_val = self.left.find_max()
            # self.data = max_val
            # self.left = self.left.delete_node(max_val)

        return self

    def inorder(self):
        element = []
        if self.left:
            element += self.left.inorder()
        element.append(self.data)
        if self.right:
            element += self.right.inorder()
        return element

    def preorder(self):
        element = [self.data]
        if self.left:
            element += self.left.preorder()
        if self.right:
            element += self.right.preorder()
        return element

    def postorder(self):
        element = []
        if self.left:
            element += self.left.postorder()
        if self.right:
            element += self.right.postorder()

        element.append(self.data)
        return element

    def search(self, key):
        if self.data == key:
            return True
        elif self.data > key:
            if self.left:
                return self.left.search(key)
            else:
                return False
        else:
            if self.right:
                return self.right.search(key)
            else:
                return False

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def calc_sum(self):
        ls = 0
        if self.left:
            ls = self.left.calc_sum()
        rs = 0
        if self.right:
            rs = self.right.calc_sum()
        return self.data + ls + rs


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BSTNode(elements[0])

    for i in range(1, len(elements)):
        root.insert_node(elements[i])

    return root


if __name__ == '__main__':
    # countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    # country_tree = build_tree(countries)
    #
    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))
    # print("In order traversal gives this sorted list:", country_tree.inorder())
    # country_tree.display()
    # country_tree.delete_node(value='China')
    # country_tree.display()

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("Min:", numbers_tree.find_min())
    print("Max:", numbers_tree.find_max())
    print("Sum:", numbers_tree.calc_sum())
    print("In order traversal:", numbers_tree.inorder())
    print("Pre order traversal:", numbers_tree.preorder())
    print("Post order traversal:", numbers_tree.postorder())
    numbers_tree.display()
    numbers_tree.delete_node(value=17)
    numbers_tree.display()
