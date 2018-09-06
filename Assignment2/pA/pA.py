import sys

a = int(sys.argv[1])
exp = int(sys.argv[3])
mod = int(sys.argv[2])
'''
with open("input002.txt") as f:
    t = f.readline()
bits = list()
bits = t.split(" ")
a = 88
exp = 3
mod = 41
'''
xp = bin(exp)[2:]
s = 0

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
sq = a
xp = reverse(xp)
if int(xp[0]) == 1:
        s += a % mod
else:
    s = 1
for x in range(1, len(xp)):
    sq = (sq**2) % mod
    if int(xp[x]) == 1:
        s = (s * sq) % mod
s = (s % mod)
print("" + str(a) + " ^ " + str(exp) + " mod " + str(mod) + " = "+ str(s) + "")
