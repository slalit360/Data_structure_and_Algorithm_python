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
            min_val = self.right.find_min()  # find min from right sub tree
            self.data = min_val  # replace min with self data
            self.right = self.right.delete_node(min_val)  # remove min from right sub tree recursively

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

    @staticmethod
    def _build_tree_string(root, curr_index, index=False, delimiter='-'):
        """Recursively walk down the binary tree and build a pretty-print string.

        In each recursive call, a "box" of characters visually representing the
        current (sub)tree is constructed line by line. Each line is padded with
        whitespaces to ensure all lines in the box have the same length. Then the
        box, its width, and start-end positions of its root node value repr string
        (required for drawing branches) are sent up to the parent call. The parent
        call then combines its left and right sub-boxes to build a larger box etc.

        :param root: Root node of the binary tree.
        :type root: binarytree.Node
        :param curr_index: Level-order_ index of the current node (root node is 0).
        :type curr_index: int
        :param index: If set to True, include the level-order_ node indexes using
            the following format: ``{index}{delimiter}{value}`` (default: False).
        :type index: bool
        :param delimiter: Delimiter character between the node index and the node
            value (default: '-').
        :type delimiter:
        :return: Box of characters visually representing the current subtree, width
            of the box, and start-end positions of the repr string of the new root
            node value.
        :rtype: ([str], int, int, int)

        .. _Level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
        """
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.data)
        else:
            node_repr = str(root.data)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = \
            BSTNode._build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            BSTNode._build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

        # Draw the branch connecting the current root node to the left sub-box
        # Pad the line with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root node
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root node to the right sub-box
        # Pad the line with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root repr positions
        return new_box, len(new_box[0]), new_root_start, new_root_end

    def __str__(self):
        """Return the pretty-print string for the binary tree.

        :return: Pretty-print string.
        :rtype: str | unicode

        **Example**:

        .. doctest::

            >>> from binarytree import Node
            >>>
            >>> root = Node(1)
            >>> root.left = Node(2)
            >>> root.right = Node(3)
            >>> root.left.right = Node(4)
            >>>
            >>> print(root)
            <BLANKLINE>
              __1
             /   \\
            2     3
             \\
              4
            <BLANKLINE>

        .. note::
            To include level-order_ indexes in the output string, use
            :func:`binarytree.Node.pprint` instead.

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
        """
        lines = BSTNode._build_tree_string(self, 0, False, '-')[0]
        return '\n'.join((line.rstrip() for line in lines))


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
    #numbers_tree.display()
    print(numbers_tree)
    numbers_tree.delete_node(value=17)
    #numbers_tree.display()
    print(numbers_tree)
