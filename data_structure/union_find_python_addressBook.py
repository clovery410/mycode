import collections
class UnionFind(object):
    def __init__(self):
        # create a new empty union-find sturcture
        self.parents = {}
        self.weights = {}

    def find(self, obj):
        # check for previously unknow object
        if obj not in self.parents:
            self.parents[obj] = obj
            self.weights[obj] = 1
            return obj

        # find path of objects leading to the root
        path = [obj]
        root = self.parents[obj]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        return iter(self.parents)

    def union(self, objects):
        roots = [self.find(x) for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

    def getUnionSet(self):
        unionSet = collections.defaultdict(list)
        for obj, parent in self.parents.items():
            unionSet[parent].append(obj)
        return [x for x in unionSet.values()]

class Solution(object):
    def contactDuplication(self, addressBook):
        emails = collections.defaultdict(list)
        for name, email_list in addressBook.items():
            for email in email_list:
                emails[email].append(name)
        uf = UnionFind()
        for name_group in emails.values():
            uf.union(name_group)

        return uf.getUnionSet()

if __name__ == "__main__":
    sol = Solution()
    addressBook = {"c1": ["shuw@fb.com", "shu@gmail.com"],
                   "c2": ["bob@fb.com"],
                   "c3": ["shu@gmail.com", "shuw@yahoo.com"],
                   "c4": ["shuw@yahoo.com"],
                   "c5": ["bob@fb.com"],
                   "c6": ["jamie@fb.com"]}
    print sol.contactDuplication(addressBook)
