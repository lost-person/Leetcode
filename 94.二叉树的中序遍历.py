#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        
        node_list = []
        node = root
        while node_list or node:
            if node:
                node_list.append(node)
                node = node.left
            else:
                node = node_list.pop()
                res.append(node.val)
                node = node.right
        return res
# @lc code=end

