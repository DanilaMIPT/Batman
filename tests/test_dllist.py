"""
check all the methods for DoubleLinkedList class
"""
import unittest
from app.HW2 import DoubleLinkedList

class TestDoubleLinkedList1(unittest.TestCase):
    """
    testing of push, pop, unshift, shift methods in DoubleLinkedList
    """

    # init testing
    def test_list_init(self):
        """
        init should create list with None head and tail
        """
        test_list = DoubleLinkedList()
        res = test_list.head, test_list.tail
        self.assertEqual(res, (None, None))

    # -----------------------------------------
    # push testing. There are three situations:
    # push to empty list
    # push to 1-item list
    # push to any other list

    def test_one_push_two_none(self):
        """
        pushing 1st item, head and tail become this item
        """
        lis = DoubleLinkedList()
        lis.push(1)
        head1 = lis.head.prev_item, lis.head.elem, lis.head.next_item
        self.assertTrue(bool((head1 == (None, 1, None)) & (lis.head == lis.tail)))

    def test_two_push_to_none(self):
        """
        pushing 2nd item, tail becomes new, head.next_item = tail
        """
        lis = DoubleLinkedList()
        lis.push(1)
        lis.push('abc')
        chain_head = lis.head.prev_item, lis.head.elem, \
                lis.head.next_item.elem, lis.head.next_item.next_item
        self.assertTrue(bool((chain_head == (None, 1, 'abc', None)) \
                & (lis.tail.elem == 'abc')))

    def test_three_push_to_none(self):
        """
        if list contain more then 2 items, pushing leads
        only to tail changes
        """
        lis = DoubleLinkedList()
        lis.push(1)
        lis.push('abc')
        lis.push((1, 2))
        chain_head = lis.head.elem, lis.tail.prev_item.elem, \
            lis.tail.prev_item.next_item.elem, lis.tail.next_item
        self.assertTrue(bool(chain_head == (1, 'abc', (1, 2), None)))

    # --------------------------------------------
    # unshift testing. There are three situations:
    # unshift to empty list
    # unshift to 1-item list
    # unshift to any other list

    def test_one_unshift_to_none(self):
        """
        unshifting 1st item, head and tail become this item
        """
        lis = DoubleLinkedList()
        lis.unshift(1)
        head1 = lis.head.prev_item, lis.head.elem, lis.head.next_item
        self.assertTrue(bool((head1 == (None, 1, None)) & (lis.head == lis.tail)))

    def test_two_unshift_to_none(self):
        """
        unshifting 2nd item, head becomes new, tail.prev_item = head
        """
        lis = DoubleLinkedList()
        lis.unshift(1)
        lis.unshift('abc')
        chain_head = lis.head.prev_item, lis.head.elem, \
                lis.head.next_item.elem, lis.head.next_item.next_item
        self.assertTrue(bool((chain_head == (None, 'abc', 1, None))\
                & (lis.tail.elem == 1)))

    def test_three_unshift_to_none(self):
        """
        if list contains 2+ items, adding changes only head
        """
        lis = DoubleLinkedList()
        lis.unshift(1)
        lis.unshift('abc')
        lis.unshift((1, 2))
        chain_head = lis.head.prev_item, lis.head.next_item.prev_item.elem, \
                lis.head.next_item.elem, lis.tail.elem
        self.assertTrue(bool(chain_head == (None, (1, 2), 'abc', 1)))

    # -----------------------------------
    # pop testing. There four situations:
    # pop from empty list
    # pop from 1-item list
    # pop from 2-item list
    # pop from any other list

    def test_pop_from_empty(self):
        """
        if list is empty, list doesn't change
        """
        lis = DoubleLinkedList()
        lis.pop()
        res = lis.head, lis.tail
        self.assertEqual(res, (None, None))

    def test_pop_from_one_item_list(self):
        """
        if there was only 1 item, so head = tail = None
        """
        lis = DoubleLinkedList()
        lis.push(1)
        lis.pop()
        res = lis.head, lis.tail
        self.assertEqual(res, (None, None))

    def test_pop_from_two_item_list(self):
        """
        if there were 2 items => no tail = head
        and the items around become None
        """
        lis = DoubleLinkedList()
        lis.push(1)
        lis.push('abc')
        lis.pop()
        head1 = lis.head.prev_item, lis.head.elem, lis.head.next_item
        self.assertTrue(bool((head1 == (None, 1, None)) & (lis.head == lis.tail)))

    # three is the same as any further
    def test_pop_from_tree_item_list(self):
        """
        change only tail and its previous item
        """
        lis = DoubleLinkedList()
        lis.push(1)
        lis.push('abc')
        lis.push((1, 2))
        lis.pop()
        chain_head = lis.head.prev_item, lis.head.elem, \
                lis.head.next_item.elem, lis.head.next_item.next_item
        self.assertTrue(bool((chain_head == (None, 1, 'abc', None))\
                & (lis.tail.elem == 'abc')))

    # -------------------------------------
    # shift testing. There four situations:
    # shift from empty list
    # shift from 1-item list
    # shift from 2-item list
    # shift from any other list

    def test_shift_from_empty(self):
        """
        if list is empty => nothing changes
        """
        lis = DoubleLinkedList()
        lis.shift()
        res = lis.head, lis.tail
        self.assertEqual(res, (None, None))

    def test_shift_from_one_item_list(self):
        """
        in case of 1-item list
        head = tail = None
        """
        lis = DoubleLinkedList()
        lis.push(1)
        lis.shift()
        res = lis.head, lis.tail
        self.assertEqual(res, (None, None))

    def test_shift_from_two_item_list(self):
        """
        in case of 2-item list, head = tail
        items around are None
        """
        lis = DoubleLinkedList()
        lis.push(1)
        lis.push('abc')
        lis.shift()
        head1 = lis.head.prev_item, lis.head.elem, lis.head.next_item
        self.assertTrue(bool((head1 == (None, 'abc', None))\
                & (lis.head == lis.tail)))

    # three is the same as any further
    def test_shift_from_tree_item_list(self):
        """
        change only head and next_item's prev_item
        """
        lis = DoubleLinkedList()
        lis.push(1)
        lis.push('abc')
        lis.push((1, 2))
        lis.shift()
        chain_head = lis.head.prev_item, lis.head.elem, \
                lis.head.next_item.elem, lis.head.next_item.next_item
        self.assertTrue(bool((chain_head == (None, 'abc', (1, 2), None))\
                & (lis.tail.elem == (1, 2))))

    # ------------------------------------
    # init list longList for further tests

class TestDoubleLinkedList2(unittest.TestCase):
    """
    testing of last, first, len, delete and contains methods
    """

    def setUp(self):
        """
        the list with differant types for universal testing
        """
        self.list = DoubleLinkedList()
        self.list.push(23)
        self.list.push(1)
        self.list.push('abc')
        self.list.push((1, 2))
        self.list.push(0)
        self.list.push(1)
        self.list.push(100)

    # ---------------------------------------
    # last() testing. There are 2 situations:
    # None.last()
    # any oter case

    def test_last_for_none(self):
        """
        if list is empty: the last is None
        """
        lis = DoubleLinkedList()
        res = lis.last()
        self.assertIsNone(res)

    def test_last_for_other_list(self):
        """
        return tail.elem
        """
        lis = self.list
        res = lis.last()
        self.assertEqual(res, 100)

    # ---------------------------------------
    # first() testing. There are 2 situations:
    # None.first()
    # any oter case

    def test_first_for_none(self):
        """
        if list is empty: the first is None
        """
        lis = DoubleLinkedList()
        res = lis.last()
        self.assertIsNone(res)

    def test_first_for_other_list(self):
        """
        return tail.elem
        """
        lis = self.list
        res = lis.first()
        self.assertEqual(res, 23)

    # --------------------------------------
    # len() testing. There are 2 situations:
    # None.len()
    # any otehr case

    def test_len_for_none(self):
        """
        len of empty list is 0
        """
        lis = DoubleLinkedList()
        res = lis.len()
        self.assertEqual(res, 0)

    def test_len_for_other_list(self):
        """
        check random list. In our case len = 7
        """
        lis = self.list
        res = lis.len()
        self.assertEqual(res, 7)

    # --------------------------------------
    # contains(x) testing. There are 3 case:
    # list is None
    # contains
    # doesn't contain

    def test_cont_in_none(self):
        """
        empty list can't contain anything, so False
        """
        lis = DoubleLinkedList()
        self.assertFalse(lis.contains(0))

    def test_cont_in_other(self):
        """
        if list contain, return True
        in our case list contains 'abc' so True
        """
        lis = self.list
        self.assertTrue(lis.contains('abc'))

    def test_not_cont_in_other(self):
        """
        if list doesn't contain elem: return False
        in this case list doesn't contain 2, so False
        """
        lis = self.list
        self.assertFalse(lis.contains(2))


    # -----------------------------------------------
    # delete(x, key) testing. There are 5 situations:
    # delete from None
    # delete(x) all x(key=default), containing in list
    # delete(x, n) x containing in list n times:
    #   n > real
    #   n <= real
    # delete x that is not in list
    # (no test of any key, because this test in n > real

    def test_delete_from_none(self):
        """
        you can't delete anything from empty list,
        so we need to check that head and tail are still None
        """
        lis = DoubleLinkedList()
        res = lis.head, lis.tail
        self.assertEqual(res, (None, None))

    def test_delete_all_1_in_list(self):
        """
        new list can't contain '1'as a full elem
        so check all the elements in new list
        """
        lis = self.list
        lis.delete(1)
        now = lis.head
        i = 0
        answer = (23, 'abc', (1, 2), 0, 100)
        while now is not None:
            self.assertEqual((now.elem), answer[i])
            now = now.next_item
            i += 1

    def test_delete_1_five_times(self):
        """
        there can be problems if program will try to find 1 five items
        so check that there are no bugs and all the elem in new list
        """
        lis = self.list
        lis.delete(1, 5)
        now = lis.head
        i = 0
        answer = (23, 'abc', (1, 2), 0, 100)
        while now is not None:
            self.assertEqual((now.elem), answer[i])
            now = now.next_item
            i += 1

    def test_delete_1_one_time(self):
        """
        check that only first item is deleted
        compare all the elements in new list with result
        """
        lis = self.list
        lis.delete(1, 1)
        now = lis.head
        i = 0
        answer = (23, 'abc', (1, 2), 0, 1, 100)
        while now is not None:
            self.assertEqual((now.elem), answer[i])
            now = now.next_item
            i += 1

    def test_delete_2_from_list(self):
        """
        if list doesn't contain elem, so it doesn't change
        check all the elem in new list
        """
        lis = self.list
        lis.delete(2, 1)
        now = lis.head
        i = 0
        answer = (23, 1, 'abc', (1, 2), 0, 1, 100)
        while now is not None:
            self.assertEqual((now.elem), answer[i])
            now = now.next_item
            i += 1
