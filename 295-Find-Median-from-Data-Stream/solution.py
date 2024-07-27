class MedianFinder:

    def __init__(self):
        # small: max heap
        # big: min heap
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        """
        Time: O(log n)
        Space: O(n)
        """
        # insert into small heap
        heapq.heappush(self.small, -num)

        # every num in small <= every num in big
        if self.small and self.big and -self.small[0] > self.big[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        
        # uneven size
        if len(self.small) > len(self.big) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        
        if len(self.big) > len(self.small) + 1:
            val = -heapq.heappop(self.big)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        """
        Time: O(1)
        Space: O(1)
        """
        # odd number
        if len(self.small) > len(self.big):
            return -self.small[0]
        if len(self.big) > len(self.small):
            return self.big[0]
        
        return (-self.small[0] + self.big[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()