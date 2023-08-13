# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0


    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy_head.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur = self.dummy_head
        while cur.next!=None:
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        
        cur = self.dummy_head
        while index:
            cur = cur.next
            index -= 1
        temp_Node = ListNode(val, cur.next)
        cur.next = temp_Node
        self.size += 1


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
param_1 = obj.get(1)
obj.deleteAtIndex(1)
param_2 = obj.get(1)
print()