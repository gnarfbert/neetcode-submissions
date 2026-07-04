# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # To build a map to look for the indices in inorder to 
        # determine which subtree the node belongs to
        indices = {val: idx for idx, val in enumerate(inorder)}

        # Global preorder pointer is for children of the 
        # original root.
        self.pre_idx = 0
        # left right pointer to transverse the left and right 
        # subtrees in the inorder array.
        def dfs(l, r):
            # This implies that we have finished considering the 
            # range([l,r]) in the inorder array so we can return
            if l > r:
                return None
            # fetches the value
            root_val = preorder[self.pre_idx]
            # Moves on to the next child in preorder
            self.pre_idx += 1
            # Builds node
            root = TreeNode(root_val)
            # Treat current node as a root of its own tree
            mid = indices[root_val]
            
            #Because inorder transversal divides the tree into
            #two halves the left subtree is indices from [l, root - 1]
            # and the right subtree is indices from [root + 1, r]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            #return the current root
            return root

        return dfs(0, len(inorder) - 1)