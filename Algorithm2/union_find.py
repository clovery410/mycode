class UnionFind(object):

    class Node(object):
        def __init__(self, key):
            self.key = key
            self.leader = self
            self.size = 1

    def __init__(self, lst):
        self.lst = lst
#        self.cluster = set()
        self.cluster = {}
        
        for element in lst:
#            self.cluster.add(self.Node(element))
            self.cluster[element] = self.Node(element)

    def leader_find(self, node):
        current = node
        while current.leader != current:
            current = current.leader
        return current

    def find(self, val):
        return self.leader_find(self.cluster[val])
        # for item in self.cluster:
        #     if item.key == val:
        #         return self.leader_find(item)

    def union(self, val1, val2):
        # for item in self.cluster:
        #     if item.key == val1:
        #         node1 = item
        #     if item.key == val2:
        #         node2 = item
        node1 = self.cluster[val1]
        node2 = self.cluster[val2]
        

        leader1 = self.leader_find(node1)
        leader2 = self.leader_find(node2)
        if leader1 != leader2:
            if leader1.size <= leader2.size:
                leader2.size += leader1.size
                leader1.leader = leader2
            else:
                leader1.size += leader2.size
                leader2.leader = leader1
        else:
            raise ValueError('two nodes in same cluster')


if __name__ == '__main__':
    f = open('clustering1.txt')
    content = f.read()
    lines = content.splitlines()

    num_node = int(lines[0])

    edges = list()
    clusters = set()

    for line in lines[1:]:
        node1 = int(line.split()[0])
        node2 = int(line.split()[1])
        cost = int(line.split()[2])
        edges.append((node1, node2, cost))
        clusters.add(node1)
        clusters.add(node2)

    my_uf = UnionFind(clusters)
    import operator
    edges = sorted(edges, key = operator.itemgetter(2), reverse = True)
    min_space = edges[0][2]
    size = len(clusters)

    while size > 4:
        min_edge = edges[-1]
        if my_uf.find(min_edge[0]) != my_uf.find(min_edge[1]):
            my_uf.union(min_edge[0], min_edge[1])
            size = size - 1
        edges.remove(min_edge)

    for edge in edges:
        if my_uf.find(edge[0]) != my_uf.find(edge[1]):
            space = edge[2]
            if space < min_space:
                min_space = space

    print(min_space)
            
