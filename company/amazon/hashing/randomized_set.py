class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash_map:
            return False
        
        self.hash_map[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash_map:
            return False
        
        val_index = self.hash_map[val]
        
        self.hash_map[self.list[-1]] = val_index
        self.list[val_index], self.list[-1] = self.list[-1], self.list[val_index]
        self.list.pop()
        del self.hash_map[val]
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
