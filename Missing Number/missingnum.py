class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0] == 1:
            return 0
        else:
            for i in range(0,len(nums)):
                if (nums[i] + 1) not in nums:
                    return nums[i] + 1
