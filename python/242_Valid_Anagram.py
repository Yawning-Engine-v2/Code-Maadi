class Solution:
    # slower 
    def isAnagram_1(self, s: str, t: str) -> bool:
        string_profile = {}
        len_s = len(s)
        if len_s != len(t):
            return False
        else:
            for i in range(len_s):
                string_profile[ord(s[i])] = string_profile.get(ord(s[i]), 0) + 1
                string_profile[ord(t[i])] = string_profile.get(ord(t[i]), 0) - 1
            
            return not any(string_profile.values())
    
    # faster 
    def isAnagram(self, s: str, t: str) -> bool:
        string_profile = {}
        
        if len(s) != len(t):
            return False
        else:
            for s,t in zip(s,t):
                string_profile[ord(s)] = string_profile.get(ord(s), 0) + 1
                string_profile[ord(t)] = string_profile.get(ord(t), 0) - 1
            
            return not any(string_profile.values())