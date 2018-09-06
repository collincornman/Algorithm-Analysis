import heapq
import sys
import math
txt = []
freq = {}
TotalCharacters = -1
encodedtxt = ""

with open(sys.argv[1]) as f:
  while True:
    c = f.read(1)
    txt.append(c)
    TotalCharacters +=1
    if not c in freq:
        freq[c] = 1
    else:
        freq[c] += 1
    if not c:
      break

OriginalBits = TotalCharacters * 8
def encode(freq):
    heap = [[wt, [sym, ""]] for sym, wt in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
Encoded = []
huff = encode(freq)
EncodedBits = 0
AveCodelength = 0
i = 0
j = 0
w = 0
v = 0
t = 0
Tmpdict = {}
FinalDict = {}
Ratio = 0
while i < len(huff):
    Tmpdict[i] = huff[i]
    i += 1
while j < len(Tmpdict):
    w = len(Tmpdict[j][1])
    v = freq[Tmpdict[j][0]]
    t = ((float(v) / float(OriginalBits)) * float(100))
    FinalDict[Tmpdict[j][0]] = Tmpdict[j][1], round(t,4)
    EncodedBits += w * v
    j += 1

Ratio = (float(EncodedBits) / float(OriginalBits)) * float(100)
AveCodelength = (float(Ratio) / float(100)) * float(8)

print("Character" + "        " + "Frequency" + "                   " + "Codeword")

Character = ""
Codeword = ""
Frequency = ""
for key in FinalDict:
    Character = repr(key)
    Codeword = str(FinalDict[key][0])
    Frequency = str(FinalDict[key][1])
    print(Character + "               " + Frequency + "%                " + Codeword)
print("Average Codeword Length:" + str(round(AveCodelength,4)))
print("Original Size (bits):" + str(OriginalBits))
print("Encoding Size (bits):" + str(EncodedBits))
print("Compression Ratio:" + str(round(Ratio,4)) + "%")