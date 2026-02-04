from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_list = []
        grouped_dicts = defaultdict(list)
        
        for str in strs:
            sorted_str = "".join(sorted(str))
            grouped_dicts[sorted_str].append(str)
        
        for key in grouped_dicts:
            grouped_list.append(grouped_dicts[key])
        
        return grouped_list