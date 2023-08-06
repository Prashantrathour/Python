class QueueUsingStack:
    def __init__(self):
        self.stack_enq = []
        self.stack_deq = []

    def enqueue(self, item):
        # Push all elements from the dequeue stack to the enqueue stack
        while self.stack_deq:
            self.stack_enq.append(self.stack_deq.pop())

        self.stack_enq.append(item)

    def dequeue(self):
        # Push all elements from the enqueue stack to the dequeue stack
        while self.stack_enq:
            self.stack_deq.append(self.stack_enq.pop())

        if not self.stack_deq:
            raise IndexError("Queue is empty.")

        return self.stack_deq.pop()


# Example usage:
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
