# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        from collections import deque
        
        if not root:
            return root
        queue = deque([root])
        while queue:
            prev = None
            for _ in range(len(queue)):
                cur = queue.popleft()
                if prev:
                    prev.next = cur
                prev = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root                
        
node1 = Node(4)
node2 = Node(5)
node3 = Node(6)
node4 = Node(7)
node5 = Node(2, node1, node2)
node6 = Node(3, node3, node4)
root  = Node(1, node5, node6)

solution = Solution()
root = solution.connect(root)
print(root)
