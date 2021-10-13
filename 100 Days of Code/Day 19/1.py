# 1008. Construct Binary Search Tree from Preorder Traversal (leetcode)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def insert(root, val):
            if root is None:
                return TreeNode(val)

            if root.val >= val:
                root.left = insert(root.left, val)

            if root.val < val:
                root.right = insert(root.right, val)

            return root

        root = None
        for item in preorder:
            root = insert(root, item)

        return root
