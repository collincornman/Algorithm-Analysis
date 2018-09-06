import sys
for line in open(sys.argv[1], 'r').readlines():
    s = line

def reverse(st):
    rev = ""
    for p in st:
        rev = p + rev
    return rev

n = len(s)
r = reverse(s)

def findPal(s, r, n):
    m = [0] * (n+1)
    for a in range(n+1):
        m[a] = [0] * (n+1)

    root = [0] * (n+1)
    for a in range(n+1):
        root[a] = [0] * (n+1)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == r[j-1]:
                m[i][j] = (m[i-1][j-1] + 1)
                root[i][j] = '`'
            else:
                if m[i-1][j] >= m[i][j-1]:
                    m[i][j] = m[i-1][j]
                    root[i][j] = '^'
                else:
                    m[i][j] = m[i][j-1]
                    root[i][j] = '-'
    e = ""
    a = b = n
    while a != 0 and b != 0:
        if root[a][b] == '`':
            e += s[a-1]
            a -= 1
            b -= 1
        elif root[a][b] == '^':
            a -= 1
        else:
            b -= 1
    return e

e = findPal(s, r, n)

print("Length: " + str(len(e)))
print("Sequence: " + e)
