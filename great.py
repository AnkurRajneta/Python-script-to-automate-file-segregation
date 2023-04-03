import os
import re

file_path = "C:/great"

pattern = r'('


for path,directories,files in os.walk(file_path):

    for name in files:
        jk = os.path.join(path,name)

        result = re.search(pattern, jk)
        if result:
            extracted_string = result.group(1)
            print(extracted_string)

       

