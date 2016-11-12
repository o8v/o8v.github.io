f = open("города.txt", "r", encoding="utf-8")
a = f.readlines() 

regions = dict()
for line in a:
    parts = line.split(",")
    name = parts[0]
    region = parts[1]
    size = int(parts[3])
    if region not in regions:
        regions[region] = 0
    regions[region] += size

z = []
for r in regions:
    z.append((regions[r], r))
z.sort()

for x in z:
    print(x[1], x[0])



