# stack uses LIFO concept last in first out order
# e.g : Stack of coin / function call stack frame in RAM / undo functionality
# O(1) on pop and Push
# O(n) element lookup/search
# implementation of stack in python is not recommended because of dynamic nature of list
# instead use : collection.dequeue

# Data Structure	                            Time Complexity
#                     Average	                                    Worst
#                     Access	Search	Insertion	Deletion	    Access	Search	Insertion	Deletion
# Stack	              Θ(n)	    Θ(n)	Θ(1)	    Θ(1)	        O(n)	O(n)	O(1)	    O(1)

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
        self.size = 0

    def push(self, val):
        self.container.append(val)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def get_size(self):
        return self.size

    def __str__(self):
        return "Stack : {0}".format(self.container)


stk = Stack()
print(stk)
stk.push(5)
stk.push(1)
print(stk)
stk.pop()
print(stk)
stk.push(10)
print(stk)
print(stk.peek())
print(stk.get_size())
print(stk.is_empty())
print(stk.pop())
print(stk.pop())
print(stk)
print(stk.is_empty())


# reverse string using stack
def reverse_string(string):
    stk = Stack()
    for char in string:
        stk.push(char)

    while stk.get_size() != 0:
        print(stk.pop(), end='')


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))


# checks if paranthesis in the string/expression are balanced or not

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(exp):
    stk = Stack()

    for char in exp:
        if char in ['(', '{', '[']:
            stk.push(char)
        elif char in [')', '}', ']']:
            if stk.is_empty():
                return False
            if not is_match(char, stk.pop()):
                return False
    else:
        return stk.is_empty()


if __name__ == '__main__':
    print(is_balanced("({a+b})"))  # --> True
    print(is_balanced("))((a+b}{"))  # --> False
    print(is_balanced("((a+b))"))  # --> True
    print(is_balanced("))"))  # --> False
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))  # --> True
