p, k, den = list(int(x) for x in input().split()) + [[1]]
while len(den) < p:
    den[-1] += 1
    den.append((den[-1] - 1) * den[-1])
print(den[k])
