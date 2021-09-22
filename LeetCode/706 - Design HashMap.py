class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10 ** 4
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucketIndex, chainIndex = self.__findIndexForKey(key)
        if chainIndex is -1:
            self.buckets[bucketIndex].append((key, value))
        else:
            self.buckets[bucketIndex][chainIndex] = (key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucketIndex, chainIndex = self.__findIndexForKey(key)
        if chainIndex is not -1:
            return self.buckets[bucketIndex][chainIndex][1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucketIndex, chainIndex = self.__findIndexForKey(key)
        if chainIndex is not -1:
            del self.buckets[bucketIndex][chainIndex]
        
    def __findIndexForKey(self, key: int) -> (int, int):
        bucketIndex = abs(hash(key)) % self.size
        
        for index, pair in enumerate(self.buckets[bucketIndex]):
            if pair[0] == key:
                return (bucketIndex, index)
        
        return (bucketIndex, -1)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)