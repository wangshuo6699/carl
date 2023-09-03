# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        queue.append(child)
            result.append(level)
        return result

node5 = Node(5)
node6 = Node(6)
node2 = Node(2)
node4 = Node(4)
node3 = Node(3, [node5, node6])
root = Node(1, [node3, node2, node4])

solution = Solution()
res = solution.levelOrder(root)
print(res)
