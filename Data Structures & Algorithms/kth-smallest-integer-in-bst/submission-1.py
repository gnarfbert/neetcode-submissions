# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hq = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            hq.append(root.val)
            inorder(root.right)
            return
        
        inorder(root)
        res = 0
        i = 0
        print(hq)
        while k > 0:
            res = hq[i]
            k -= 1
            i += 1
        return res

        