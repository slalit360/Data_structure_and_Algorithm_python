# one of solution for producer consumer problem
# follows FIFO concept.approach
# O(1) for insert(enqueue : append at left) and delete(dequeue : remove from right) operation
# O(n) for lookup and search operation

# Data Structure	                            Time Complexity
#                     Average	                                    Worst
#                     Access	Search	Insertion	Deletion	    Access	Search	Insertion	Deletion
# Queue	              Θ(n)	    Θ(n)	Θ(1)	    Θ(1)	        O(n)	O(n)	O(1)	    O(1)

import threading
import time
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if self.size() == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.buffer)

    def __str__(self):
        return f"Queue : {self.buffer}"


if __name__ == '__mainf__':
    queue = Queue()
    print(queue)
    queue.enqueue(5)
    print(queue)
    queue.enqueue(1)
    print(queue)
    queue.dequeue()
    print(queue)
    print(queue.size())
    print(queue.is_empty())
    queue.dequeue()
    print(queue)
    print(queue.size())
    print(queue.is_empty())


# below example is to illustrate producer consumer problem solved using queue
class Restaurant:
    food_order_queue = Queue()
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

    def place_orders(self):
        for order in self.orders:
            print("Placing order for:", order)
            self.food_order_queue.enqueue(order)
            time.sleep(1)

    def serve_orders(self):
        time.sleep(1)
        while not self.food_order_queue.is_empty():
            order = self.food_order_queue.dequeue()
            print("Now serving: ", order)
            time.sleep(2)


if __name__ == '__main__':
    rs = Restaurant()
    t1 = threading.Thread(target=rs.place_orders)
    t2 = threading.Thread(target=rs.serve_orders)

    t1.start()
    t2.start()
