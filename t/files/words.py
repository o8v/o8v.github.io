import random
f = open("города.txt", "r", encoding="utf-8")
a = f.readlines()

w = set()
d = dict()
for line in a:
    word = line.split(",")[0]
    word = "^^" + word + "$"
    w.add(word)
    for i in range(len(word)-2):
        key = word[i] + word[i + 1]
        if key not in d:
            d[key] = []
        d[key].append(word[i + 2])

for i in range(100):
    name = "^^"
    while name[-1] != "$":
        key = name[-2] + name[-1]
        z = d[key]
        name = name + z[random.randint(0, len(z) - 1)]
    if name not in w:
        print(name[2:-1])
