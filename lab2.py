class Stack:
    def init(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())