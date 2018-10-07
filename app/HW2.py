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

    # add an item at the beginning
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

    # remove an item from the beginning
    def shift(self):
        if self.head is None:
            print("I'm already empty")
        # case of 1 item list
        elif self.head.next_item is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next_item
            self.head.prev_item = None

    # return the last elem in list
    def last(self):
        if self.head is not None:
            return self.tail.elem
        else:
            return None

    # return the first elem in list
    def first(self):
        if self.head is not None:
            return self.head.elem
        else:
            return None

    #return the length of the list
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
    
    # True if list contain elem=a, else: false
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

    # with no key: delete all the item with elem=a,
    # with key=n: delete a n times
    # if n more then real number of a in list, delete only what list have
    def delete(self, a, k=-1):
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

