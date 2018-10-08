"""
realisation of DoubleLinkedList class
"""
class Item:
    """
    this elements of this class are part of DoubleLinkedList
    """
    def __init__(self, data, next_item=None, prev_item=None):
        """
        init new item. next and prev items are None by default
        elem is necessery for input
        """
        self.elem = data
        self.next_item = next_item
        self.prev_item = prev_item


class DoubleLinkedList:
    """
    this list contains items with links to next and previous items
    also list include head and tail of list
    """

    def __init__(self):
        """
        in new list there must be head = tail = None
        """
        self.head = None
        self.tail = None

    def push(self, elem):
        """
        add an item at the end
        """
        new = Item(elem, None, self.tail)
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

    def pop(self):
        """
        remove an item from the end
        """
        if self.head is None:
            print("I'm already empty")
        # case of 1 item list
        elif self.head.next_item is None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev_item
            self.tail.next_item = None

    def unshift(self, elem):
        """
        add an item at the beginning
        """
        new = Item(elem, self.head, None)
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
        """
        remove an item from the beginning
        """
        if self.head is None:
            print("I'm already empty")
        # case of 1 item list
        elif self.head.next_item is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next_item
            self.head.prev_item = None

    def last(self):
        """
        return the last elem in list
        """
        if self.head is not None:
            return self.tail.elem
        return None

    def first(self):
        """
        return the first elem in list
        """
        if self.head is not None:
            return self.head.elem
        return None

    def len(self):
        """
        return the length of the list
        """
        size = 0
        now = self.head
        if now is None:
            return 0
        while now is not None:
            size += 1
            now = now.next_item
        return size

    def contains(self, elem):
        """
        True if list contain elem, else: false
        """
        now = self.head
        if now is None:
            return False
        while now is not None:
            if elem == now.elem:
                return True
            now = now.next_item
        return False

    def delete(self, elem, k=-1):
        """
        with no key: delete all the item with elem=a,
        with key=n: delete a n times
        if n more then real number of a in list, delete real number
        """
        now = self.head
        counter = 0
        if now is None:
            return()
        while now is not None:
            if now.elem == elem:
                counter += 1
                if now.next_item is None:
                    self.pop()
                elif now.prev_item is None:
                    self.shift()
                else:
                    now.prev_item.next_item = now.next_item
                    now.next_item.prev_item = now.prev_item
            now = now.next_item
            if counter == k:
                return()
