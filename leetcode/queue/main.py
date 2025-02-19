class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [None] * k
        self.head = self.tail = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
            
        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = value
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
            return True
        
        self.head = (self.head + 1) % self.size
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.tail]
    
    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head


def main():
    my_queue = MyCircularQueue(3)
    print(my_queue.enQueue(1))
    print(my_queue.enQueue(2))
    print(my_queue.enQueue(3))
    print(my_queue.enQueue(4))
    print(my_queue.Rear())
    print(my_queue.isFull())
    print(my_queue.deQueue())
    print(my_queue.enQueue(4))
    print(my_queue.Rear())


if __name__ == '__main__':
    main()
