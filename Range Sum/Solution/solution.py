# O(NlogN) greedy solution w/ sorting
# Author: Avnith Vijayram

# Sort the N numbers
# Find the K - 1 largest differences between adjacent numbers 
# Separate into groups based on those differences

from heapq import heappush, heappop

N, K = map(int, input().split())
x = [int(x) for x in input().split()]
x.sort()
heep = []
for i in range(N - 1):
    heappush(heep, (x[i] - x[i + 1], i))

brks = set()
for _ in range(K - 1):
    brks.add(heappop(heep)[1])
brks.add(N - 1)

ls = []
for i, num in enumerate(x):
    ls.append(str(num))
    if i in brks:
        print(' '.join(ls))
        ls = []
