/*
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
TreeNode* kSmallest(TreeNode* root, int& count, int k) 
{ 
    if (root == NULL) 
        return NULL; 
  
    TreeNode* left = kSmallest(root->left, count, k); 
  
    if (left != NULL) 
        return left; 
  
    count++; 
    if (count == k) 
        return root; 
   
    return kSmallest(root->right, count, k); 
}
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;
        TreeNode* res = kSmallest(root, count, k); 
        return res->val;
    }
};
