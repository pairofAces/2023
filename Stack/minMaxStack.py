# Min Max Stack Construction

'''
Write a MinMaxStack class for a Min Max Stack. The class should support:
- Pushing and popping values on and off the stack
- Peeking at the value at the top of the stack
- Getting both the minimum and the maximum values in the stack at any 
  given point in time.

All class methods, when considered independently, should run in constant time and
with constant space. 
'''

class MinMaxStack():
    # initialize the class
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    # This is required to be O(1) time | O(1) space
    # This function will provide the topmost value of the stack
    def peek(self):
        return self.stack[len(self.stack) - 1]  # Note - how a stack works

    # This is required to be O(1) time | O(1) space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # This is required to be O(1) time | O(1) space
    def push(self, num):
        newMinMax = {"min": num, "max": num}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], num)
            newMinMax["max"] = max(lastMinMax["max"], num)
        
        self.minMaxStack.append(newMinMax)
        self.stack.append(num)
        
    def getMin(self):
        pass

    def getMax(self):
        pass