class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pretty_s1 = ''.join(sorted(s1))
        window_size = len(pretty_s1)
        start_p = 0
        end_p = start_p + window_size
        while end_p <= len(s2):
            #print("Current Window:", ''.join(sorted(s2[start_p:end_p])))
            if ''.join(sorted(s2[start_p:end_p])) == pretty_s1:
                return True
            end_p += 1
            start_p += 1
        else:
            return False