import sys
import math
i = -1;
sets = [];
items = set();
keys = []
fre = []
S = []
child = []
for line in open("input001.txt", 'r').readlines():
    if(i==-1):
        n = int(line.strip());
    elif(i < n):
        tokens = line.strip().split(" ")
        itemset = []
        keys.append(tokens[0])
        fre.append(tokens[1])
        for x in tokens:
          item = x.strip()
          itemset.append(item)
          items.add(item)
        sets.append(itemset)
    i=i+1

keys.sort()
sets.sort()
freqs = []

for x in range(0, len(sets)):
    freqs.append(sets[x][1])


def sumFreq(f,i, j):
    sum = 0
    for x in range(i, j):
        sum += float(f[x])
    return sum

root = [0]* (n)
for b in range(n):
    root[b] = [0]*(n)

matrix = [0] * (n+1)
for a in range(n+1):
    matrix[a] = [0] * (n+1)

for i in range(n+1):
    for j in range(n+1):
        if j - i == 1:
            matrix[i][j] = float(freqs[i])

for i in range(n):
    for j in range(n):
        if j - i == 0:
            root[i][j] = i


for d in range(1, n+1):
    for i in range(1, (n+1)-d):
        j = i + d
        mini = float("inf")
        for k in range(i, j+1):
            q = float(matrix[i-1][k-1]) + float(matrix[k][j])
            if q < mini:
                mini = q
                root[i-1][j-1] = k-1
        matrix[i-1][j] = mini + sumFreq(freqs, i-1, j)

r = root[0][n-1]
S.append((r, 0, n-1))
while S:
    (u, i, j) = S.pop()
    k = root[i][j]
    if k < j:
        v = root[k+1][j]
        S.append((v, k+1, j))
        child.append((keys[u],keys[v], k, j))
    if i < k:
        v = root[i][k-1]
        S.append((v, i, k-1))
        child.append((keys[u], keys[v], i, k))

print("C =")
for x in range(len(matrix)):
    sys.stdout.write("[")
    for y in range(len(matrix[x])):
        sys.stdout.write(" " + "{0:.3f}".format(matrix[x][y]))
    print("]")

print("")

print("R =")
for x in range(len(root)):
    sys.stdout.write("[")
    for y in range(len(root[x])):
        sys.stdout.write(" " + "{0:.0f}".format(float(root[x][y])))
    print("]")
print("")

def printNode(k, childs, set):
    parent = "(null)"
    lc = None
    rc = None
    freq = 0
    for x in set:
        if x[0] == k:
            freq = x[1]
    for x in childs:
        if x[1] == k:
            parent = x[0]
        if x[0] == k:
            if x[2] < keys.index(k):
                lc = x[1]
            else:
                rc = x[1]
    print("Node")
    print("   Key: " + k)
    print("   Probability: " + str("{0:.2f}".format(float(freq)*100) + "%"))
    print("   Parent: " + str(parent))
    print("   Left Child:" + str(lc))
    print("   Right Child: " + str(rc))

for x in keys:
    printNode(x, child, sets)



