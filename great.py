import os
path = "C:/scope"
os.startfile(path)
l = []
for s in os.walk(path):
        l.append(s)
for name in l:
    print(name)

