class LRUReplace():
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0
        self.cache = {}
        self.lru = {}

    def is_exist(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.counter += 1
            return self.cache[key]
        return -1

    def update(self, key, value):
        if len(self.cache) >= self.capacity:
            _toReplace = min(self.lru.keys(), key = lambda x: self.lru[k])
            del self.cache[_toReplace]
            del self.lru[_toReplace]
        self.cache[key] = value
        self.lru[key] = self.counter
        self.counter += 1

