class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            for i in nums:
                nums.append(nums.pop(nums.index(0)))
