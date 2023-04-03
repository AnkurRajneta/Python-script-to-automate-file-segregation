import os

root = "C:/great"

for path,directories,files in os.walk(root):
    for name in files:
        print(os.path.join(path,name))
