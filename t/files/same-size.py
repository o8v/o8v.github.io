
f = open("города.txt", "r", encoding="utf-8")
a = f.readlines() 

z = dict()
for line in a:
    parts = line.split(",")
    name = parts[0]
    size = int(parts[3])
    if size not in z:
        z[size] = []
    z[size].append((name, parts[1]))

for size in z:
    if len(z[size]) > 1:
        print(size, z[size])




