f = open('tsp.txt')

content = f.read()
lines = content.splitlines()

num = int(lines[0])
vertex = list()
coordiantor = list()

for i in range(num):
    vertex.append(i)
    
for line in lines[1:]:
    x = float(line.split()[0])
    y = float(line.split()[1])
    coordinator.append((x, y))

print(vertex)
print(coordinator)

import itertools
def dp_tsp(vertex, n):
    a = [[MAX for j in range(n)] for s in set(itertools.combinations(vertex, n))]
    if 0 in S and len(S) == 1:
        a[S][0] = 0
    else:
        a[S][0] = MAX

    for m in range(1, n):
        for S in set(itertools.combinations(vertex.remove(0), m)):
            for j in S
