mod = 1000000000039
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

infile = open("input.txt", 'r')
outfile = open("output.txt", 'w')
Q = int(infile.readline())
for i in range(Q):
    N = int(infile.readline())
    lcm = 1
    for x in map(int, infile.readline().split()):
        lcm *= (x // gcd(lcm, x))
        lcm %= mod
    outfile.write(str(lcm) + "\n")

infile.close()
outfile.close()