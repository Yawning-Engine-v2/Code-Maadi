class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_list = list(sorted(count.items(), key=lambda x: x[1], reverse=True))
        
        top_k_list = list()
        for i in range(0,k):
            top_k_list.append(sorted_list[i][0]) 
        
        return top_k_list
        