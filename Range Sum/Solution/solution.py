# O(NlogN) greedy solution w/ sorting
# Author: Avnith Vijayram

# Sort the N numbers
# Find the K - 1 largest differences between adjacent numbers 
# Separate into groups based on those differences

from heapq import heappush, heappop
from sys import stdout

inp = open("input.txt", 'r')
wr = open("output.txt", 'w')

N, K = map(int, inp.readline().split())
x = [int(x) for x in inp.readline().split()]
x.sort()

heep = []
for i in range(N - 1):
    heappush(heep, (x[i] - x[i + 1], i))

brks = set()
for _ in range(K - 1):
    brks.add(heappop(heep)[1])
brks.add(N - 1)

ls = []
z = 0
for i, num in enumerate(x):
    ls.append(str(num))
    if i in brks:
        wr.write(' '.join(ls) + ("\n" if i != N - 1 else ""))
        ls = []
inp.close()
wr.close()
