class MapIterator(object):
    def __init__(self, nestedMap):
        self.stack = []
        for elem in reversed(nestedMap.values()):
            self.stack.append(elem)

    def next(self):
        return self.stack.pop()

    def hasNext(self):
        while self.stack:
            if type(self.stack[-1]) != dict:
                return True
            top_nested_map = self.stack.pop()
            for elem in reversed(top_nested_map.values()):
                self.stack.append(elem)
        return False

if __name__ == "__main__":
    nested_map = {1: {2: {}, 3: {4: "Hello"}}, 5: "word"}
    mi = MapIterator(nested_map)
    while mi.hasNext():
        print mi.next()
