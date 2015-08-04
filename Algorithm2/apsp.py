MAX = 99999
f = open('g3.txt')

content = f.read()
lines = content.splitlines()

num_v = int(lines[0].split()[0])
num_e = int(lines[0].split()[1])

edge = {}
cache = {}
min_path = list()

for line in lines[1:]:
    tail = int(line.split()[0]) - 1
    head = int(line.split()[1]) - 1
    cost = int(line.split()[2])
    edge[(tail, head)] = cost
    
print(edge)

def bellman(edge, n):
    l = [[MAX for v in range(n)] for i in range(n + 1)]
    min_result = MAX

    for s in range(n):
        print('current s is: %d' % s)
        for i in range(n + 1):
            to_break = True
            for v in range(n):
                if i == 0 and v == s:
                    l[i][v] = 0

                if i == 0 and v != s:
                    l[i][v] = MAX

                if i > 0:
                    min_previous = MAX
                    for w in range(n):
                        if (w, v) in edge and (l[i - 1][w] + edge[(w, v)]) < min_previous :
                            min_previous = l[i - 1][w] + edge[(w, v)]
                    
                    l[i][v] = min(l[i - 1][v], min_previous)
                    if l[i][v] != l[i - 1][v]:
                        to_break = False
                        
                if l[i][v] < min_result:
                    min_result = l[i][v]

                if i == n and l[i][v] != min_result:
                    print('NULL')
                    raise ValueError('It has negative cycle')
                        
            if to_break and i != 0:
                break
#        print(min_result)
#        import pdb
#        pdb.set_trace()


        min_path.append((s, min_result))
    return min_result

            
def floyd(edge, n):
    print ('ffff')
    a = [[[MAX for k in xrange(num_v)] for j in xrange(num_v)] for i in xrange(num_v)]
    print ('bbbb')
    min_value = MAX
    for k in range(n):
        print('Current k is: %d' % k)
        for i in range(n):
            for j in range(n):
#                print('Before: a[%d][%d][%d]: %d' % (i, j, k, a[i][j][k]))

                if k == 0:
                    if i == j:
                        a[i][j][k] = 0
                    elif (i, j) in edge:
                        a[i][j][k] = edge[(i, j)]
                    else:
                        a[i][j][k] = MAX
                else:
                    a[i][j][k] = min(a[i][j][k-1], a[i][k][k-1] + a[k][j][k-1])

 #               print('After: a[%d][%d][%d]: %d' % (i, j, k, a[i][j][k]))

                if a[i][j][k] < min_value:
                    min_value = a[i][j][k]
                if k == n - 1 and i == j and a[i][j][k] < 0:
                    print('NULL')
                    raise ValueError('had negative cycle')

    return min_value

result = bellman(edge, num_v)
print(result)


