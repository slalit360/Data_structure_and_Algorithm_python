class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        print("------ SinglyLinkedList ------")

    def insert_beg(self, value):
        self.head = Node(data=value, next=self.head)

    def insert_end(self, value):
        if self.head is None:
            self.head = Node(data=value)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data=value, next=None)

    def insert_at(self, index, value):
        if 0 > index or index >= self.get_count():
            print("Invalid index")
        elif 0 == index:
            # print("insert_beg")
            self.insert_beg(value=value)
        else:
            count = 0
            itr = self.head
            while itr.next:
                if count == index - 1:
                    itr.next = Node(data=value, next=itr.next)
                    break
                itr = itr.next
                count += 1

    def insert_values(self, values_list, init=False):
        if init:
            self.head = None
        for ele in values_list:
            self.insert_end(ele)

    def insert_after_value(self, data_after, data_to_insert):
        try:
            data_after_idx = self.get_index(value=data_after) + 1
            self.insert_at(index=data_after_idx, value=data_to_insert)
        except:
            pass

    def remove_by_value(self, value):
        self.remove_at(index=self.get_index(value=value))

    def remove_at(self, index):
        if 0 > index or index >= self.get_count():
            print("Invalid index")
        elif index == 0:
            self.head = self.head.next
        else:
            count = 0
            itr = self.head
            while itr.next:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def get_count(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def get_index(self, value):
        itr = self.head
        count = 0
        while itr:
            if itr.data == value:
                # print(f"index of {value} : {count}")
                return count
            itr = itr.next
            count += 1
        else:
            print(f"ValueError : {value} does not found!")

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        temp = []
        count = 0
        itr = self.head
        while itr:
            temp.append(f"{count}[{itr.data}]")
            itr = itr.next
            count += 1
        print(*temp, sep=" -> ", end=" -> NULL\n")


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        print("------ DoublyLinkedList ------")

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_beg(self, value):
        node = Node(data=value, next=self.head, prev=None)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert_end(self, value):
        if self.head is None:
            self.head = Node(data=value)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data=value, next=None, prev=itr)

    def insert_at(self, index, value):
        if 0 > index or index >= self.get_count():
            print("Invalid index")
        elif 0 == index:
            # print("insert_beg")
            self.insert_beg(value=value)
        else:
            count = 0
            itr = self.head
            while itr.next:
                if count == index - 1:
                    node = Node(data=value, next=itr.next, prev=itr)
                    if node.next:
                        node.next.prev = node
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def insert_values(self, values_list, init=False):
        if init:
            self.head = None
        for ele in values_list:
            self.insert_end(ele)

    def insert_after_value(self, data_after, data_to_insert):
        try:
            data_after_idx = self.get_index(value=data_after) + 1
            self.insert_at(index=data_after_idx, value=data_to_insert)
        except:
            pass

    def insert_before_value(self, data_before, data_to_insert):
        try:
            data_idx = self.get_index(value=data_before)
            self.insert_at(index=data_idx, value=data_to_insert)
        except:
            pass

    def remove_by_value(self, value):
        self.remove_at(index=self.get_index(value=value))

    def remove_at(self, index):
        if 0 > index or index >= self.get_count():
            print("Invalid index")
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            count = 0
            itr = self.head
            while itr.next:
                if count == index:
                    itr.prev.next = itr.next
                    if itr.next:
                        itr.next.prev = itr.prev
                    break
                itr = itr.next
                count += 1

    def get_count(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def get_index(self, value):
        itr = self.head
        count = 0
        while itr:
            if itr.data == value:
                # print(f"index of {value} : {count}")
                return count
            itr = itr.next
            count += 1
        else:
            print(f"ValueError : {value} does not found!")

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        temp = []
        count = 0
        itr = self.head
        while itr:
            temp.append(f"{count}[{itr.data}]")
            itr = itr.next
            count += 1
        print(*temp, sep=" <=> ", end=" <=> NULL\n")

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty!")
            return

        last_node = self.get_last_node()
        temp = []
        itr = last_node
        while itr:
            temp.append(f"[{itr.data}]")
            itr = itr.prev
        print(*temp, sep=" <=> ", end=" <=> NULL\n")


if __name__ == '__main__':
    ll = SinglyLinkedList()
    ll.insert_beg(11)
    ll.insert_beg(13)
    ll.insert_beg(15)
    ll.insert_end(100)
    ll.insert_values(values_list=[11, 13, 15, 100], init=True)
    ll.print_ll()
    print("Length :", ll.get_count())
    ll.insert_at(index=3, value=500)
    ll.print_ll()
    ll.insert_at(index=0, value=999)
    ll.print_ll()
    ll.insert_at(index=ll.get_count()-1, value=9999)
    ll.print_ll()
    print("Length :", ll.get_count())
    ll.remove_at(index=0)
    ll.print_ll()
    ll.remove_at(index=ll.get_count()-1)
    ll.print_ll()
    print("Length :", ll.get_count())
    ll.get_index(value=100)
    ll.insert_after_value(data_after=15, data_to_insert=8989)
    ll.print_ll()
    ll.insert_after_value(data_after=500, data_to_insert=9999)
    ll.print_ll()
    ll.remove_by_value(value=15)
    ll.print_ll()

    dl = DoublyLinkedList()
    dl.insert_beg(100)
    dl.print_forward()
    dl.insert_beg(500)
    dl.print_forward()
    dl.insert_end(200)
    dl.print_forward()
    dl.insert_beg(600)
    dl.print_forward()
    dl.insert_at(index=3, value=999)
    dl.print_forward()
    dl.remove_at(index=1)
    dl.print_forward()
    dl.insert_after_value(data_after=100, data_to_insert=101010)
    dl.print_forward()
    dl.insert_before_value(data_before=100, data_to_insert='hello')
    dl.print_forward()
    dl.remove_by_value(value='hello')
    dl.print_forward()
    dl.print_backward()
