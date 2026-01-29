from typing import List

#310/315 timeout
class Solution:
    def two_sum(self, nums, target):
        map = dict()
        #print(nums)
        target = -target
        return_list = []
        for i in range(len(nums)):
            map[nums[i]] = i
        
        for i in range(len(nums)):
            val = map.get(target-nums[i],0)
            if val != i and val !=0:
                #print([nums[i],nums[val]])
                return_list.append([nums[i],nums[val]])

        return return_list


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        final_list = []
        for i in range(len(nums)):
            target = nums[i]
            #print("Target:",target)
            new_nums = nums[:]
            new_nums.pop(i)
            two_lists = self.two_sum(new_nums, target)
            if two_lists == None or two_lists == []:
                continue
            else:
                for two_list in two_lists:
                    if target + two_list[0] + two_list[1] == 0:
                        if sorted((target,two_list[0],two_list[1])) in final_list:
                            pass
                        else:
                            final_list.append(sorted((target,two_list[0],two_list[1])))
        return (final_list)
    
