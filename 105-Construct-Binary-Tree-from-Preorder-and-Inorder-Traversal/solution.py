# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Time: O(n ^ 2)
        Space: O(n)
        """
        # base case
        if not preorder or not inorder:
            return None
        
        # root: 1st element of preorder
        root = TreeNode(val=preorder[0])

        # retrieve index of root in inorder list
        mid = inorder.index(preorder[0])
        
        # recursive case
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root