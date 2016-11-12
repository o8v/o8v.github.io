f = open("города.txt", "r", encoding="utf-8")
a = f.readlines() 
c = []
for line in a:
    parts = line.split(",")
    name = parts[0]
    size = int(parts[3])
    c.append((-size, name))
c.sort()

fout = open("порядок.txt", "w", encoding="utf-8")
for city in c:
    print(city[1], -city[0], file = fout)
fout.close()


