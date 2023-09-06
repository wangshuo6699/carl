# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # 层序遍历
        from collections import deque

        depth = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.children:
                    for child in cur.children:
                        queue.append(child)
            depth += 1
        return depth
            
        # 后序遍历
        # if not root:
        #     return 0
        # if not root.children:
        #     return 1
        # depths = []
        # for child in root.children:
        #     depths.append(self.maxDepth(child))
        # return 1+max(depths)
        
node5 = Node(5)
node6 = Node(6)
node2 = Node(2)
node4 = Node(4)
node3 = Node(3, [node5, node6])
root = Node(1, [node3, node2, node4])

solution = Solution()
res = solution.maxDepth(root)
print(res)
