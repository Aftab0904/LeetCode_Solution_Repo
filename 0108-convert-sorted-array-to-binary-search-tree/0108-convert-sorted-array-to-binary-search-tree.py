# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return None

        mid_point=len(nums)//2
        return TreeNode(nums[mid_point],self.sortedArrayToBST(nums[:mid_point]),self.sortedArrayToBST(nums[mid_point+1:]))





