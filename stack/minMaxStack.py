class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    # O(1) | O(1)
    def peek(self):
        return self.stack[-1]

    # O(1) | O(1)
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) | O(1)
    def push(self, number):

        self.stack.append(number)

        if len(self.minMaxStack) == 0:
            new_min = number
            new_max = number
        else:
            new_min = min(number, self.minMaxStack[-1]["min"])
            new_max = max(number, self.minMaxStack[-1]["max"])

        self.minMaxStack.append({
            "min": new_min,
            "max": new_max
        })

    # O(1) | O(1)
    def getMin(self):
        return self.minMaxStack[-1]["min"]

    # O(1) | O(1)
    def getMax(self):
        return self.minMaxStack[-1]["max"]


if __name__ == "__main__":
    stack = MinMaxStack()
    stack.push(5)
    stack.push(1)
    stack.push(10)

    print(stack.getMax())