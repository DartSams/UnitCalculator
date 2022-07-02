from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import random
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver=webdriver.Chrome(r'chromedriver.exe', options=options)
conversion_dict = {}
volume_lst = [
    "gallon",
    "US_liquid_quart",
    "US_liquid_pint",
    "US_legal_cup",
    "US fluid ounce",
    "US_tablespoon",
    "US_teaspoon",
    "Cubic_meter",
    "Liter",
    "Milliliter",
    "Imperial_gallon",
    "Imperial_quart",
    "Imperial_pint",
    "Imperial_cup",
    "Imperial_fluid ounce",
    "Imperial tablespoon",
    "Imperial teaspoon",
    "Cubic_foot",
    "Cubic_inch",
]

volume_lst2 = volume_lst.copy() #makes a copy of the first list


# for i in volume_lst:
#     driver.implicitly_wait(5)
#     conversion_dict[i] = {}
#     if i in volume_lst2: #needed to remove duplicate from 2nd list to be scraped without messing up googles layout then placeholder will be placed back into 2nd list
#         placeholder = i
#         volume_lst2.remove(i)
#     for j in volume_lst2: #needed to iterate through all of the elements in the 2nd list while holding onto 1 element in the first list at a time
#         time.sleep(3) #needed because the scraper will move to fast so google will think its a robot making queries
#         # s = f"convert {i} to {j}"
#         driver.get(str(f"https://www.google.com/search?q=convert+{i}+to+{j}")) #uses google search query
#         # time.sleep(5)
#         # driver.implicitly_wait(10)
#         conversion_string = driver.find_element(By.CLASS_NAME,"bjhkR").text.split(" ") #finds the div with this classname to return the conversion description
#         # print(conversion_string)
#         print(i,j,conversion_string)
#         name = "to_" + j
#         conversion_dict[i][name] = {}
#         conversion_dict[i][name]["conversion_num"] = float(conversion_string[-1])
#         if "multiply" in conversion_string:
#             conversion_dict[i][name]["operation"] = "multiply"

#         elif "divide" in conversion_string:
#             conversion_dict[i][name]["operation"] = "divide"


#         # print(f"convert {i} to {j}")
#     volume_lst2.append(placeholder)

#     # break

# # print(conversion_dict)

# with open('volume.json', 'w') as fp:
#     json.dump(conversion_dict, fp,indent=4)
    


