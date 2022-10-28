import random

Nmx = 10 ** 5
Kmn = 10
Kmx = 200
diff = 100
xmx = 10 ** 9

with open("input.txt", 'w') as wr:
    N = random.randrange(Nmx - diff, Nmx)
    K = random.randrange(Kmn, Kmx)
    wr.write(str(N) + " " + str(K) + "\n")
    written = set()
    written.add(0)
    for i in range(N):
        x = 0
        while x in written: x = random.randrange(1, xmx + 1)
        wr.write(str(x) + " ")
    