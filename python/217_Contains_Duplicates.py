class Solution:
    def containsDuplicate_1(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num) > 1:
                return True
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            num_set.add(num)

        return len(num_set) != len(nums)
    