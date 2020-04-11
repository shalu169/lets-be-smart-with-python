class MaxHeap:
    def __init__(self, items = []):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatup(len(self.heap)-1)
    def __floatup(self, id):
        parent = id//2
        if parent <= 1:
            return
        elif self.heap[parent] > self.heap[id]:
            self.swap(id, parent)
            self.__floatup(parent)
    def pop(self):
        if len(self.heap)>2:
            self.swap(1,len(self.heap)-1)
            max = self.heap.pop()
            self.__bubble_down(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = None
        return max
    def swap(self, in1, in2):
        self.heap[in1],self.heap[in2] = self.heap[in2], self.heap[in1]
    def push(self, value):
        self.heap.append(value)
        self.__floatup(len(self.heap)-1)
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            False
    def __bubble_down(self, ind):
        left = ind * 2
        right = ind * 2 +1
        largest = ind
        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != ind:
            self.swap(ind, largest)
            self.__bubble_down(largest)
    def __str__(self):
        return str(self.heap)
m = MaxHeap([3,21,95])
print(m)
m.push(10)
print(m)
m.push(100)
print(m)
m.push(97)
print(m)




