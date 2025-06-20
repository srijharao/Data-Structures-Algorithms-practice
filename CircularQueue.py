class MyCircularQueue:

    def __init__(self, k: int):
        self.data = []
        self.head = 0
        self.tail = 0
        self.num_elements = 0
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if self.num_elements == 0:
            self.data.append(value)
            self.head = 0
            self.num_elements += 1
            return True
        elif self.num_elements < self.k:
            self.data.append(value)
            self.tail = len(self.data)-1
            self.num_elements += 1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.head] = 0
        self.head += 1
        self.num_elements -= 1
        return True
        
        

    def Front(self) -> int:
        if self.num_elements != 0:
            return self.data[self.head]
        return -1
        

    def Rear(self) -> int:
        if self.num_elements != 0:
            return self.data[self.tail]
        return -1
        

    def isEmpty(self) -> bool:
        if self.num_elements == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.num_elements == self.k:
            return True
        return False
        


# MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


#input:
#["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
#[[3],[1],[2],[3],[4],[],[],[],[4],[]]

#expected o/p:
# [null,true,true,true,false,3,true,true,true,4]
