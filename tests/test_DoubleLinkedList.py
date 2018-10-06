from app.HW2 import *
import unittest

class TestMyClass(unittest.TestCase):

    # init testing 
    def test_listInit(self):
        dList = DoubleLinkedList()
        res = dList.head, dList.tail
        self.assertEqual(res, (None, None))
    
    #-----------------------------------------
    # push testing. There are three situations:
    # push to empty list
    # push to 1-item list
    # push to any other list

    def test_onePushToNone(self):
        a = DoubleLinkedList()
        a.push(1)
        head1 = a.head.prev_item, a.head.elem, a.head.next_item
        self.assertTrue(bool((head1 == (None, 1, None)) & (a.head == a.tail))) 
    
    def test_twoPushToNone(self):
        a = DoubleLinkedList()
        a.push(1)
        a.push('abc')
        chainHead = a.head.prev_item, a.head.elem, \
                a.head.next_item.elem, a.head.next_item.next_item
        self.assertTrue(bool((chainHead == (None, 1, 'abc', None)) & (a.tail.elem == 'abc')))

    def test_threePushToNone(self):
        a = DoubleLinkedList()
        a.push(1)
        a.push('abc')
        a.push((1, 2))
        chainHead = a.head.elem, a.tail.prev_item.elem, \
                a.tail.prev_item.next_item.elem, a.tail.next_item
        self.assertTrue(bool(chainHead == (1, 'abc', (1, 2), None)))

    #--------------------------------------------
    # unshift testing. There are three situations:
    # unshift to empty list
    # unshift to 1-item list
    # unshift to any other list

    def test_oneUnshiftToNone(self):
        a = DoubleLinkedList()
        a.unshift(1)
        head1 = a.head.prev_item, a.head.elem, a.head.next_item
        self.assertTrue(bool((head1 == (None, 1, None)) & (a.head == a.tail)))

    def test_twoUnshiftToNone(self):
        a = DoubleLinkedList()
        a.unshift(1)
        a.unshift('abc')
        chainHead = a.head.prev_item, a.head.elem, \
                a.head.next_item.elem, a.head.next_item.next_item
        self.assertTrue(bool((chainHead == (None, 'abc', 1, None)) & (a.tail.elem == 1)))

    def test_threeUnshiftToNone(self):
        a = DoubleLinkedList()
        a.unshift(1)
        a.unshift('abc')
        a.unshift((1, 2))
        chainHead = a.head.prev_item, a.head.next_item.prev_item.elem, \
                a.head.next_item.elem, a.tail.elem
        self.assertTrue(bool(chainHead == (None, (1, 2), 'abc', 1)))
    
    #-----------------------------------
    # pop testing. There four situations:
    # pop from empty list
    # pop from 1-item list
    # pop from 2-item list
    # pop from any other list

    def test_popFromEmpty(self):
        a = DoubleLinkedList()
        a.pop()
        res = a.head, a.tail
        self.assertEqual(res, (None, None))

    def test_popFromOneItemList(self):
        a = DoubleLinkedList()
        a.push(1)
        a.pop()
        res = a.head, a.tail
        self.assertEqual(res, (None, None))

    def test_popFromTwoItemList(self):
        a = DoubleLinkedList()
        a.push(1)
        a.push('abc')
        a.pop()
        head1 = a.head.prev_item, a.head.elem, a.head.next_item
        self.assertTrue(bool((head1 == (None, 1, None)) & (a.head == a.tail)))

    # three is the same as any further
    def test_popFromTreeItemList(self):
        a = DoubleLinkedList()
        a.push(1)
        a.push('abc')
        a.push((1, 2))
        a.pop()
        chainHead = a.head.prev_item, a.head.elem, \
                a.head.next_item.elem, a.head.next_item.next_item
        self.assertTrue(bool((chainHead == (None, 1, 'abc',  None)) & (a.tail.elem == 'abc')))

    #-------------------------------------
    # shift testing. There four situations:
    # shift from empty list
    # shift from 1-item list
    # shift from 2-item list
    # shift from any other list

    def test_shiftFromEmpty(self):
        a = DoubleLinkedList()
        a.shift()
        res = a.head, a.tail
        self.assertEqual(res, (None, None))

    def test_shiftFromOneItemList(self):
        a = DoubleLinkedList()
        a.push(1)
        a.shift()
        res = a.head, a.tail
        self.assertEqual(res, (None, None))

    def test_shiftFromTwoItemList(self):
        a = DoubleLinkedList()
        a.push(1)
        a.push('abc')
        a.shift()
        head1 = a.head.prev_item, a.head.elem, a.head.next_item
        self.assertTrue(bool((head1 == (None, 'abc', None)) & (a.head == a.tail)))

    # three is the same as any further
    def test_shiftFromTreeItemList(self):
        a = DoubleLinkedList()
        a.push(1)
        a.push('abc')
        a.push((1, 2))
        a.shift()
        chainHead = a.head.prev_item, a.head.elem, \
                a.head.next_item.elem, a.head.next_item.next_item
        self.assertTrue(bool((chainHead == (None, 'abc', (1, 2), None))\
                & (a.tail.elem == (1, 2))))

    #------------------------------------
    # init list longList for further tests

    def setUp(self):
        self.list = DoubleLinkedList()
        self.list.push(23)
        self.list.push(1)
        self.list.push('abc')
        self.list.push((1, 2))
        self.list.push(0)
        self.list.push(1)
        self.list.push(100)

    #---------------------------------------
    # last() testing. There are 2 situations:
    # None.last()
    # any oter case

    def test_lastForNone(self):
        a = DoubleLinkedList()
        res = a.last()
        self.assertIsNone(res)

    def test_lastForOtherList(self):
        a = self.list
        res = a.last()
        self.assertEqual(res, 100)

    #---------------------------------------
    # first() testing. There are 2 situations:
    # None.first()
    # any oter case

    def test_firstForNone(self):
        a = DoubleLinkedList()
        res = a.last()
        self.assertIsNone(res)

    def test_firstForOtherList(self):
        a = self.list
        res = a.first()
        self.assertEqual(res, 23)

    #--------------------------------------
    # len() testing. There are 2 situations:
    # None.len()
    # any otehr case

    def test_lenForNone(self):
        a = DoubleLinkedList()
        res = a.len()
        self.assertEqual(res, 0)

    def test_lenForOtherList(self):
        a = self.list
        res = a.len()
        self.assertEqual(res, 7)

    #--------------------------------------
    # contains(a) testing. There are 3 case:
    # list is None
    # contains
    # doesn't contain

    def test_contInNone(self):
        a = DoubleLinkedList()
        self.assertFalse(a.contains(0))

    def test_contInOther(self):
        a = self.list
        self.assertTrue(a.contains('abc'))

    def test_notContInOther(self):
        a = self.list
        self.assertFalse(a.contains(2))



