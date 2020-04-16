
# Note: This Queue class is sub-optimal. Why?
# b/c self.que is using array
# time complexity to pop off first index in array is O(n) (shifts all over  1 at time )
# LL or DEQ maybe be tter


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


class Stack():
    def __init__(self):
        self.stack = []  # can get around resizing if know size of stack/create size of stack

    def push(self, value):
        self.stack.append(value)  # resizing may occur every now & then O(n)?

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()  # not espensive rt, to pop off end of -array
        else:
            return None

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)
