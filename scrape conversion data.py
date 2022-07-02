from email.mime import image
from matplotlib.font_manager import json_load
from numpy import character
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import random
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver=webdriver.Chrome(r'chromedriver.exe', options=options)
character_dict = {}
lst = [
    "US_gallon",
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
    "Imperial_tablespoon",
    "Imperial_teaspoon",
    "Cubic_foot",
    "Cubic_inch",
]

lst2 = lst #makes a copy of the first list


for i in lst:
    driver.implicitly_wait(5)
    if i in lst2: #needed to remove duplicate from 2nd list to be scraped without messing up googles layout then placeholder will be placed back into 2nd list
        placeholder = i
        lst2.remove(i)
    for j in lst2: #needed to iterate through all of the elements in the 2nd list while holding onto 1 element in the first list at a time
        driver.implicitly_wait(2)
        # s = f"convert {i} to {j}"
        driver.get(str(f"https://www.google.com/search?q=convert+{i}+to+{j}")) #uses google search query
        conversion_string = driver.find_element(By.CLASS_NAME,"bjhkR") #finds the div with this classname to return the conversion description
        print(conversion_string.text)

        # print(f"convert {i} to {j}")
    lst2.append(placeholder)

    break
    
#TODO
##manipulate conversion_string.text to make "foot/minute":{
                                                # "to_miles/hour":{
                                                #     "conversion_num":88,
                                                #     "operation":"divide"
                                                # }


