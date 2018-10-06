class Item:
    def __init__(self, data, next=None, prev=None):
        self.elem = data
        self.next_item = next
        self.prev_item = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # add an item at the end
    def push(self, a):
        new = Item(a, None, self.tail)
        # in case of empty list head is tail
        if self.head is None:
            self.head = new
            self.tail = new
        # in case of 1 item list change only head.next_item
        else:
            self.tail.next_item = new
            self.tail = new
            if self.head.next_item is None:
                self.head.next_item = new

    # remove an item from the end
    def pop(self):
        if self.head is None:
            print("I'm already empty")
        # case of 1 item list
        elif self.head.next_item is None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev_item
            self.tail.next_item = None

    def unshift(self, a):
        new = Item(a, self.head, None)
        # in case of empty list head is tail
        if self.head is None:
            self.head = new
            self.tail = new
        # in case empty => silence
        elif self.head is not None:
            self.head.prev_item = new
            self.head = new
            if self.tail.prev_item is None:
                self.tail.prev_item = new

    def shift(self):
        if self.head is None:
            print("I'm already empty")
        # case of 1 item list
        elif self.head.next_item is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next_item
            self.head.prev_item = None

    def last(self):
        if self.head is not None:
            return self.tail.elem
        else:
            return None

    def first(self):
        if self.head is not None:
            return self.head.elem
        else:
            return None

    def len(self):
        size = 0
        x = self.head
        if x is None:
            return 0
        else:
            while x is not None:
                size += 1
                x = x.next_item
            return size

    def contains(self, a):
        x = self.head
        if x is None:
            return False
        else:
            while x is not None:
                if a == x.elem:
                    return True
                x = x.next_item
            return False

    def delete(self, a, k=1):
        x = self.head
        counter = 0
        if x is None:
            return()
        else:
            while x is not None:
                if x.elem == a:
                    counter += 1
                    if x.next_item is None:
                        self.pop()
                    elif x.prev_item is None:
                        self.shift()
                    else:
                        x.prev_item.next_item = x.next_item
                        x.next_item.prev_item = x.prev_item
                x = x.next_item
                if counter == k:
                    return()


a = DoubleLinkedList()
#a.push(1)
#a.push(2)
#b = a
#a.push(3)
#print(b.tail.elem)
a.pop()
print(a.head, a.tail)
#a.unshift(1)
#a.push(5)
#a.unshift(4)
#a.push(3)
#a.push(1)
#x = a.head
#while x is not None:
#    print(x.elem)
#    x = x.next_item
#a.delete(1, 5)

#print(a.contains(1))
#x = a.head
#while x is not None:
#    print(x.elem)
#    x = x.next_item

