start = list(input().split())
max = list((int(x) for x in start[1].split(":")))
max = max[2] + 60 * max[1] + 3600 * max[0]
l = []
for x in range(int(start[0])):
    l.append(list(int(x) for x in input().split(":")))

for index, val in enumerate(l):
    l[index] = val[2] + 60 * val[1] + 3600 * val[0]

l.sort()

count = 0
tick = 0
while count <= max:
    if len(l) > 0:
        count += l[0]
    else:
        print(tick)
        exit()
    try:
        l = l[1:]
    except Exception:
        print(tick)
        exit()
    tick += 1

print(tick - 1)
