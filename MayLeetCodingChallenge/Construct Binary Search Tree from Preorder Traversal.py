"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""
def constructBST(root,val):
    if root:
        if val<root.val:
            if root.left:
                constructBST(root.left,val)
            else:
                root.left=TreeNode(val)
        else:
            if root.right:
                constructBST(root.right,val)
            else:
                root.right=TreeNode(val)

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root=TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            constructBST(root,preorder[i])
        return root
