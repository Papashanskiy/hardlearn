from queue import Queue


class MovingAverage:

    def __init__(self, size: int):
        self.queue = Queue(maxsize=size)

    def next(self, val: int) -> float:
        if self.queue.full():
            self.queue.get()
        self.queue.put(val)
        return sum(self.queue.queue) / self.queue.qsize()
    

if __name__ == '__main__':
    my_obj = MovingAverage(3)
    print(my_obj.next(1))    
    print(my_obj.next(10))    
    print(my_obj.next(3))    
    print(my_obj.next(5))
