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
    clusters.add((node1, ))
    clusters.add((node2, ))

import operator
edges = sorted(edges, key = operator.itemgetter(2), reverse = True)
min_space = edges[0][2]

while len(clusters) > 4:
    min_edge = edges[-1]
    for cluster in clusters:
        if min_edge[0] in cluster:
            c1 = cluster
        if min_edge[1] in cluster:
            c2 = cluster
    if not c1 == c2:
        clusters.add(tuple(set(c1) | set(c2)))
        clusters.remove(c1)
        clusters.remove(c2)

    edges.remove(min_edge)

for edge in edges:
    for cluster in clusters:
        if (edge[0] in cluster and edge[1] not in cluster):
            space = edge[2]
            if space < min_space:
                min_space = space
        

print(min_space)
#import pdb
#pdb.set_trace()

