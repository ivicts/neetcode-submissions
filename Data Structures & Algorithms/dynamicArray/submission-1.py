class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = []*self.capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size + 1 > self.capacity:
            self.resize()
        self.arr.append(n)
        self.size += 1
        

    def popback(self) -> int:
        n = self.arr[-1]
        self.size -= 1
        self.arr = self.arr[:-1]
        return n

    def resize(self) -> None:
        self.arr = self.arr + self.capacity*[]
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity