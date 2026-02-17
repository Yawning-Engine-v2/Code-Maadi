from typeing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperature_index_stack = []
        temperature_count = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if i == 0:
                temperature_index_stack.append(i)
                continue
    
            while len(temperature_index_stack) > 0:
    
                if temperatures[i] > temperatures[temperature_index_stack[-1]]:
                    temperature_count[temperature_index_stack[-1]] = i - temperature_index_stack[-1]
                    temperature_index_stack.pop()
                else:
                    break
            
            temperature_index_stack.append(i)
            
        if len(temperature_index_stack) > 0:
            for index in temperature_index_stack:
                temperature_count[index] = 0

        return temperature_count