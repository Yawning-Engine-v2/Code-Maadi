class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = nums[:]
        for i in range(0,len(nums)):
            num = nums[i]
            diff = target - num

            if diff in nums[i+1:]:
                return [nums.index(num), nums.index(diff,i+1)]
