class MyCircularQueue:

    def __init__(self, k: int):
        self.len = k
        self.head = 0
        self.tail = 0
        self.list = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.list[self.tail % self.len] = value
        self.tail += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.list[self.head % self.len]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.list[(self.tail - 1) % self.len]

    def isEmpty(self) -> bool:
        return (self.tail - self.head) == 0

    def isFull(self) -> bool:
        return abs(self.tail - self.head) == self.len


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# size = 3
# 1 -> 2 -> 3 (Rear)