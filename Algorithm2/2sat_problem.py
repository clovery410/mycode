from collections import defaultdict
from itertools import groupby
import resource
import sys
import time

sys.setrecursionlimit(10 ** 6)
#resource.setrlimit(resource.RLIMIT_STACK, (2 ** 19, 2 ** 20))

class Track(object):
    def __init__(self):
        self.explored = set()
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}

def dfs(graph_dict, node, track):
    track.explored.add(node)
    track.leader[node] = track.current_source
    for head in graph_dict[node]:
        if head not in track.explored:
            dfs(graph_dict, head, track)
    track.current_time += 1
    track.finish_time[node] = track.current_time

def dfs_loop(graph_dict, nodes, track):
    for node in nodes:
        if node not in track.explored:
            track.current_source = node
            dfs(graph_dict, node, track)

def scc(graph, reverse_graph, nodes):
    out = defaultdict(list)
    track = Track()
    dfs_loop(reverse_graph, nodes, track)
    sorted_nodes = sorted(track.finish_time, key = track.finish_time.get, reverse = True)
    track.current_time = 0
    track.current_source = None
    track.explored = set()
    dfs_loop(graph, sorted_nodes, track)
    for lead, vertex in groupby(sorted(track.leader, key = track.leader.get), key = track.leader.get):
        out[lead] = list(vertex)
    return out

def scc_load(filename):
    f = open(filename)
    content = f.read()
    lines = content.splitlines()
    edges = list()

    for line in lines:
        value1 = int(line.split()[0])
        value2 = int(line.split()[1])
        edges.append([value1, value2])

    nodes = list(set([v - 1 for edge in edges for v in edge]))
    G = {i: [] for i in range(len(nodes))}
    Grev = {i: [] for i in range(len(nodes))}
    for edge in edges:
        if edge[0] - 1 in G:
            G[edge[0] - 1] += [edge[1] - 1]
        else:
            G[edge[0] - 1] = [edge[1] - 1]
        if edge[1] - 1 in Grev:
            Grev[edge[1] - 1] += [edge[0] - 1]
        else:
            Grev[edge[1] - 1] = [edge[0] - 1]

    return G, Grev, nodes

def loaddata(filename):
    f = open(filename)
    content = f.read()
    lines = content.splitlines()
    num = int(lines[0])
    edges = list()

    for line in lines[1:]:
        value1 = int(line.split()[0])
        value2 = int(line.split()[1])
        edges.append([-value1, value2])
        edges.append([-value2, value1])

    nodes = list(set([v for edge in edges for v in edge]))

    G = {i - num: [] for i in range(2 * num + 1)}
    Grev = {i - num: [] for i in range(2 * num + 1)}

    for edge in edges:
        if edge[0] in G:
            G[edge[0]] += [edge[1]]
        else:
            G[edge[0]] = [edge[1]]
        if edge[1] in Grev:
            Grev[edge[1]] += [edge[0]]
        else:
            Grev[edge[1]] = [edge[0]]

    return G, Grev, nodes

def check_sat(out, nodes):

    for element in out:
        if len(out[element]) > 1:
            for value in out[element]:
                if -value in out[element] and value in nodes and -value in nodes:
                    for i in out[element]:
                        print('%d: %s' % (i, G[i]))
                    raise ValueError('Not satifibale!')
    print('Satified')

filename = '2sat6.txt'
#scc_filename = 'scc_testcase.txt'

#G, Grev, nodes = scc_load(scc_filename)
G, Grev, nodes = loaddata(filename)
#print(nodes)
#print(G)

result = scc(G, Grev, nodes)

check_sat(result, nodes)
