class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque([])
        self.cur_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.cur_sum += val
        while len(self.queue) > self.size:
            self.cur_sum -= self.queue.popleft()
        return self.cur_sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)