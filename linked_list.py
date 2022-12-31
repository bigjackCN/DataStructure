class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        tmp = self.head
        pre = self.head
        while tmp.next:
            pre = tmp
            tmp = tmp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tmp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return tmp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp

    def set_value(self, index, value):
        tmp = self.get(index)
        if tmp:
            tmp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        tmp = self.get(index - 1)
        new_node.next = tmp.next
        tmp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        tmp = prev.next
        prev.next = tmp.next
        tmp.next = None
        self.length -= 1
        return tmp

    def reverse(self):
        tmp = self.head
        self.head = self.tail
        self.tail = tmp
        after = tmp.next
        before = None
        for _ in range(self.length):
            after = tmp.next
            tmp.next = before
            before = tmp
            tmp = after
