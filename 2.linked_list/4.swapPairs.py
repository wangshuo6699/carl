# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList(object):
    def __init__(self):
        # 先初始化一个头节点，为None
        self.head = None

    # 链表初始化函数, 方法类似于尾插
    def initList(self, data):
        # 创建头结点
        # 这个节点创建完，包含两部分：是个既包含节点值，也包含节点所链接的下一个节点
        self.head = ListNode(data[0])

        # 初始化p指向头节点
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            # 构建完一个节点，移动到构建完的节点上，继续向后构建节点
            p = p.next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0, head)
        cur = dummy_head
        while cur.next!=None and cur.next.next!=None:
            temp_head1 = cur.next
            temp_head2 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = temp_head1
            cur.next.next.next = temp_head2
            cur = cur.next.next
        return dummy_head.next

l = LinkList()
l.initList([1,2,3,4])
solution = Solution()
solution.swapPairs(l.head)
