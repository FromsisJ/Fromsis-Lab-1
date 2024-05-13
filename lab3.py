class Queue:
    def init(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def is_empty(self):
        return len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()

    def peek(self):
        if self.is_empty():
            return None

        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack[-1]


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



queue = Queue()


queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)


print(queue.dequeue())
print(queue.dequeue())


queue.enqueue(40)
queue.enqueue(50)


print(queue.peek())

print(queue.dequeue())
print(queue.dequeue())

print(queue.is_empty())

print(queue.dequeue())

print(queue.is_empty())