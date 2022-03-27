from random import randint
class RandomizedSet:

    def __init__(self):
        self.rset = {}
        self.arr = []
        self.arr_len = -1
        self.n = -1

    def insert(self, val: int) -> bool:
        if val in self.rset and self.rset[val] != -1:
            return False
        else:
            self.n += 1
            self.rset[val] = self.n
            if self.n <= self.arr_len: # if no. of elements at present are less than the total array len
                self.arr[self.n] = val
            else:
                self.arr.append(val)
                self.arr_len += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.rset and self.rset[val] >= 0:
            self.arr[self.rset[val]] = self.arr[self.n]  # replacing the last element with deleted element
            self.rset[self.arr[self.n]] = self.rset[val]  # updating index of last element
            self.rset[val] = -1 
            self.n -= 1
            return True
        return False

    def getRandom(self) -> int:
        x = randint(0, self.n)
        return self.arr[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()