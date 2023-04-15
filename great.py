import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome()
driver.get('https://google.com')






# for path,directories,files in os.walk(file_path):

#     for name in files:
#         jk = os.path.join(path,name)

#         result = re.search(pattern, jk)
#         if result:
#             extracted_string = result.group(1)
#             print(extracted_string)


wait = WebDriverWait(driver, 10)

# Find the element by class name
element_list = []
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "workingit"))) 
