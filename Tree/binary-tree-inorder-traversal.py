"""
94. Binary Tree Inorder Traversal
Medium

2603

113

Add to List

Share
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder_array = []
        stack  = []
        if not root:
            return None
        temp = root
        while True:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                if stack:
                    temp = stack.pop()
                    inorder_array.append(temp.val)
                    temp = temp.right
                else:
                    return inorder_array
                
        return inorder_array
