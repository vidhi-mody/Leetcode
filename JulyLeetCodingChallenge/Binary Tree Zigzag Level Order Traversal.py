"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        answer = [[root.val]]
        i = 0
        while queue:
            depth = len(queue)
            l = []
            i = i + 1
            while depth:
                front = queue.pop(0)
                depth = depth - 1

                if front.left:
                    queue.append(front.left)
                    l+=[front.left.val]
                if front.right:
                    queue.append(front.right)
                    l+=[front.right.val]
            if l:
                if i%2==1:
                    l = l[::-1]
                answer.append(l)

        return answer