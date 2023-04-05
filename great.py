import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
driver = webdriver.Chrome()
driver.get('https://chromium')



# pattern = r'([^/\\]+)(?:\.\w+)?\s+from'


# for path,directories,files in os.walk(file_path):

#     for name in files:
#         jk = os.path.join(path,name)

#         result = re.search(pattern, jk)
#         if result:
#             extracted_string = result.group(1)
#             print(extracted_string)

Examples = driver.find_elements_by_xpath()    
Examples_list = []
for p in range(len(Examples)):
    Examples_list.append(Examples[p].text)

