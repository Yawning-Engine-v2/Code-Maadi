class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = set()
        longest_string_length = 0
        l,r = 0,0

        while r<len(s):
            if s[r] not in longest_string:
                longest_string.add(s[r])
                r += 1
            else:
                longest_string.remove(s[l])
                l += 1
            
            if len(longest_string) > longest_string_length:
                longest_string_length = len(longest_string)

        return longest_string_length
