class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'[':']','{':'}','(':')'}
        last_open = list()
        
        if (s[0] not in brackets.keys()) or (len(s)%2 != 0):
            return False
            
        for bracket in s:
            if bracket in brackets.keys():
                last_open.append(bracket)
            elif bracket in brackets.values():
                if len(last_open)<1 or (bracket != brackets[last_open[-1]]):
                    return False
                else:
                    last_open.pop()
        else:
            if len(last_open) > 0:
                return False
            else:
                return True
