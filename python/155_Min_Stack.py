class MinStack:

    def __init__(self):
        self.stack = list()
        self.top_index = int(-1)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_index += 1 
        
    def pop(self) -> None:
        self.top_index -= 1
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[self.top_index]
    
    def getMin(self) -> int:
        min = self.stack[0]
        for i in range(self.top_index+1):
            if self.stack[i] < min:
                min = self.stack[i]
        return min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(5)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()