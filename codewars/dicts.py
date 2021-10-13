from collections import defaultdict
names = ["peek", "aka", "kaka"]
d = {}
for n in names:
    key = len(n)
    print(d)

    d.setdefault(key, []).append(n)
    print(d)
    print('\n')
