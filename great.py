import os
path = "C:/great"
os.startfile(path)
l = []
for root,directories,file in os.walk(path):
        for files in file:
                l.append(os.path.join(root,file))

for f in l:
        print(f)

