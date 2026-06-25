class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.small, -num)

        if (self.small and self.large and self.large[0] < -self.small[0]):
            num = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            num = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, num)

        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*num)

    def findMedian(self) -> float:
        
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0])/2
        