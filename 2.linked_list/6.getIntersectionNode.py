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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = 0
        curA = headA
        while curA:
            l1 += 1
            curA = curA.next
        l2 = 0
        curB = headB
        while curB:
            l2 += 1
            curB = curB.next
        if l1<l2:
            l1, l2 = l2, l1
            headA, headB = headB, headA
        gap = l1-l2
        curA = headA
        curB = headB
        while gap:
            curA = curA.next
            gap -= 1
        while curA:
            if curA==curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None


        
listA = [4,1,8,4,5]
listB = [5,0,1,8,4,5]
headA = LinkList()
headA.initList(listA)
headB = LinkList()
headB.initList(listB)

solution = Solution()
res = solution.getIntersectionNode(headA.head, headB.head)
print(res)
