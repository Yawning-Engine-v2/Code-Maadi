class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        longest_window = 0
        start, end = 0, 0
        window_length = end - start + 1

        for end in range(len(s)):
            count[ord(s[end]) - 65] += 1
            window_length = end - start + 1

            while window_length - max(count) > k:
                count[ord(s[start]) - 65] -= 1
                start += 1
                window_length = end - start + 1

            longest_window = max(longest_window, window_length)       
        
        return longest_window