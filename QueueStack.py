from types import new_class


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)

new_moving_avg = MovingAverage(5)

new_moving_avg.next(7)
new_moving_avg.next(6)
new_moving_avg.next(10)
new_moving_avg.next(2)
new_moving_avg.next(2)
print(new_moving_avg.next(45))