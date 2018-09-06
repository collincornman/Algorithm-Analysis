import networkx as nx
import sys
import heapq
graph = nx.Graph()
i = -1
for line in open("input001.txt").readlines():
    if(i == -1):
        n = int(line.strip())
    else:
        tokens = line.strip().split(" ")
        graph.add_edge(int(tokens[0]), int(tokens[1]), weight=float(tokens[2]),)
    i += 1

def dfs(graph, s):
    Q = []
    Q.append(s)
    S = set()
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(sorted(graph[u],reverse = True))
        yield u

print("Depths First Search: \n" + str(list(dfs(graph,0))))

def bfs(graph, s):
    P = {s: None}
    Q = list()
    Q.append(s)
    while Q:
        u = Q.pop(0)
        sure = dict(list(graph[u].items()).sort(key=lambda x: x[1]['weight']))
        for v in sure:
            if v in P:
                continue
            P[v] = u
            Q.append(v)
    return P

print("\n Breadth First Search: \n" + str(list(bfs(graph,0))))

def mst(graph):
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    E = list()
    V = graph.nodes()
    k = 0
    temp = list()
    n = 0
    while len(E) < (len(graph.nodes())-1):
        temp = list(bfs(graph, edges[k][0]))
        n = len(temp)
        if temp[0] not in E and temp[n-1] not in E:
            E.append(edges[k])
        k = k + 1
    return(V, E)

butt = mst(graph)
print("\nMinimum Spanning Tree:")
print("V = " + str(butt[0]))

butter = ""
tot = 0
for x in butt[1]:
    tot += x[2]['weight']
    butter = butter + "(" + str(x[0]) + ", " + str(x[1])+ ", " + str(x[2]['weight']) + ")"
print("E = "+ butter)
print("Total Weight: " + str(tot))
def dij(g, s):
    h = [(0, s)]
    path = {}
    visited = {s: 0}
    n = set(g.nodes())
    while n and h:
        currW, min = heapq.heappop(h)
        try:
            while min not in n:
                currW, min = heapq.heappop(h)
        except IndexError:
            break
        n.remove(min)
        for v in g[min]:
            weight = currW + g[min][v]['weight']
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min
    return visited, path
print("\n Shortest Paths:")
rebuild = []
for x in graph:
    lst = dij(graph,x)
    #print(lst[0], lst[1])
    for y in lst[1]:
        if (lst[1][y], y) not in rebuild:
            rebuild.append((x, lst[1][y], y, lst[0][y]))
restructure = rebuild
used = []
for x in restructure:
    if (x[2], x[1]) not in used:
        if(x[2], x[0]) not in used:
            used.append((x[0], x[2]))
for x in range(len(graph.nodes())):
    for y in rebuild:
        if y[0] == x:
            if (y[0], y[2]) in used:
                print(str(y[0]) + " -> " + str(y[2]) + " = (" + str(y[0]) + ", " + str(y[2]) + ", " + str(y[3]) + ") \n  Path Weight = " + str(y[3]))