import random

M = 10 ** 6
Nmx = 100
Qmx = 2000
diff = 100
pr = 20
nr = 10

seeve = [False for i in range(M + 1)]
primes = []
for i in range(2, M + 1):
    if seeve[i]: continue
    primes.append(i)
    for i in range(i, M + 1, i):
        seeve[i] = True
np = len(primes)

with open("input.txt", 'w') as wr:
    Q = random.randrange(Qmx - diff, Qmx)
    wr.write(str(Q) + "\n")
    for i in range(Q):
        N = random.randrange(i * Nmx // Qmx, Nmx)
        wr.write(str(N) + "\n")
        for j in range(N):
            ni = None
            if j > random.randrange(0, N):
                ni = random.choice(primes[max(0, j - pr) * np // Nmx: min(np - 1, j + pr) * np // Nmx])
            else:
                ni = random.randrange(max(0, j - nr) * M // Nmx, min(np - 1, j + nr) * M // Nmx)
            wr.write(str(ni) + (" " if j != N - 1 else "\n"))
 
