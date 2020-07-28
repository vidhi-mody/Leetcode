"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def rec(inorder):
            if len(postorder):
                value = postorder[-1]
                node = TreeNode(value)
                if value not in inorder: return None
                pos = inorder.index(value)
                postorder.pop()
                node.right = rec(inorder[pos + 1:])
                node.left = rec(inorder[0:pos])
                return node
        return rec(inorder)