from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def find(self, root, nums, k):
        if(root is None):
            return False
        if(k - root.val in nums):
            return True
        nums.add(root.val)
        return self.find(root.left, nums, k) or self.find(root.right, nums, k)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        return self.find(root, nums, k)

Solution().findTarget(TreeNode(val=10), 100)