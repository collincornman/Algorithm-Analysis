import sys
i = 1;
weights = list()
temp = list()
temp2 = list()
values = list()
n = 0
W = 0
for line in open(sys.argv[1], 'r').readlines():
    if(i==1):
        n, W = line.strip().split(" ");
    elif(i == 2):
        temp = line.strip().split(" ")
    else:
        temp2 = line.strip().split(" ")
    i=i+1;

for i in temp:
    weights.append(int(i))

for j in temp2:
    values.append(int(j))

n = int(n)
W = int(W)

def knapsack(w, v, W, n):
    m = [0] * (W)
    for a in range(n+1):
        m[a] = [0] * (W + 1)

    root = [False]*(W+1)
    for b in range(n+1):
        root[b] = [False]*(W + 1)

    for k in range(1, n+1):
        i = k-1
        for r in range(1, W+1):
            m[k][r] = m[k-1][r]
            bad = m[k-1][r]
            if w[i] <= r:
                good = int(v[i]) + m[k - 1][r - w[i]]
                m[k][r] = max(bad, good)
                root[k][r] = good > bad
    return m, root


items = set()
m, q = knapsack(weights, values, W, n)
k = len(weights)
l = W
items = set()

while k != 0 and l != 0:
    i = k-1
    if q[k][l]:
        items.add(i)
        l -= weights[i]
    k -= 1


print("Tableau: ")
for x in range(len(weights)+1):
    sys.stdout.write("[")
    for y in range(len(m[x])):
        sys.stdout.write(" " + "{0:.3f}".format(m[x][y]))
    print("]")
items = list(items)
orig = []
opt = []
tot = 0
totW = 0

print("Maximum Capacity: W = " + str(W))

for x in range(len(weights)):
    orig.append((x+1, weights[x], float(values[x])))
print("Original Knapsack Items: " + str(orig))
for x in items:
    opt.append(orig[x])
print("The Optimal Solution: " + str(opt))

for x in range(len(items)):
    tot += values[items[x]]
    totW += weights[items[x]]
print("Optimal Weight: " + str(totW))
print("Optimal Value: " + str(tot))

