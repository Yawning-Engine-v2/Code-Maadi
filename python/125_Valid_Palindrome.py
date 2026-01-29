class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str =""
        for ch in s:
            asci = ord(ch)
            if (asci >=ord('a') and asci <=ord('z')) or (asci >=ord('0') and asci <=ord('9')):
                new_str += ch

        str_len = len(new_str)
        str_div_len = len(new_str)//2

        if str_len% 2 == 0:
            return new_str[:str_div_len] == new_str[str_div_len:][::-1]
        else:
            return new_str[:str_div_len] == new_str[str_div_len+1:][::-1]

