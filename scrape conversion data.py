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
mass_lst = [
    "Metric ton",
    "Kilogram",
    "Gram",
    "Milligram",
    "Microgram",
    "Imperial ton",
    "Us ton",
    "Stone",
    "Pound",
    "Ounce",
]


unit_dict = {
    "volume":volume_lst,
    "mass":mass_lst
}

def scrape_conversion_data(lst):
    copied_list = lst.copy() #makes a copy of the first list
    conversion_dict = {}
    for i in lst:
        driver.implicitly_wait(5)
        conversion_dict[i] = {}
        if i in copied_list: #needed to remove duplicate from 2nd list to be scraped without messing up googles layout then placeholder will be placed back into 2nd list
            placeholder = i
            copied_list.remove(i)
        for j in copied_list: #needed to iterate through all of the elements in the 2nd list while holding onto 1 element in the first list at a time
            time.sleep(3) #needed because the scraper will move to fast so google will think its a robot making queries
            # s = f"convert {i} to {j}"
            driver.get(str(f"https://www.google.com/search?q=convert+{i}+to+{j}")) #uses google search query
            conversion_string = driver.find_element(By.CLASS_NAME,"bjhkR").text.split(" ") #finds the div with this classname to return the conversion description
            # print(conversion_string)
            # print(i,j,conversion_string)
            name = "to_" + j
            conversion_dict[i][name] = {}
            if "e+" in conversion_string[-1]: #this will check if the conversion number is in scientific notation and will convert it to python syntax not necessary because python does this automatically but is placed here for extra clarification (handling all cases)
                conversion_num_placeholder = conversion_string[-1].split("e+")
                conversion_num = float(conversion_num_placeholder[0])*10**int(conversion_num_placeholder[-1])
                conversion_dict[i][name]["conversion_num"] = float(conversion_num)

            elif "e+" not in conversion_string[-1]:
                conversion_dict[i][name]["conversion_num"] = float(conversion_string[-1])

            if "multiply" in conversion_string:
                conversion_dict[i][name]["operation"] = "multiply"
                print(i,j,"multiply by ",str(conversion_dict[i][name]["conversion_num"]))

            elif "divide" in conversion_string:
                conversion_dict[i][name]["operation"] = "divide"
                print(i,j,"divide by ",str(float(conversion_num)))

            # print(f"convert {i} to {j}")
        copied_list.append(placeholder)

    # break

    with open('mass.json', 'w') as fp:
        json.dump(conversion_dict, fp,indent=4)


# scrape_conversion_data(unit_dict["mass"])