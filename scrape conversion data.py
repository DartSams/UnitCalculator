from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.chrome.options import Options
import itertools

options = Options()
options.headless = (
    True  # this stops the browser from opening every time the file is run
)

driver = webdriver.Chrome(r"chromedriver.exe", options=options)

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
pressure_lst = [
    "Bar",
    "Pascal",
    "Pound-force/inch squared",
    "Standard atmosphere",
    "Torr",
]
frequency_lst = ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"]
energy_lst = [
    "Joule",
    "Kilojoule",
    "Gram_calorie",
    "kilo_calorie",
    "Watt_hour",
    "Kilo_watt_hour",
    "Electron_volt",
    "British_thermal_unit",
    "US_therm",
    "Foot_pound",
]
time_lst = [
    "Nanosecond",
    "Microsecond",
    "Millisecond",
    "Second",
    "Minute",
    "Hour",
    "Day",
    "Week",
    "Month",
    "Calendar year",
    "Decade",
    "Century",
]
fuel_lst = [
    "Miles/gallon",
    "Imperial_Miles/gallon",
    "Kilometer/liter",
]
temperature_lst = ["Fahrenheit", "Celsius", "Kelvin"]

unit_dict = {
    "volume": volume_lst,
    "mass": mass_lst,
    "pressure": pressure_lst,
    "fuel": fuel_lst,
    "frequency": frequency_lst,
    "energy": energy_lst,
    "time": time_lst,
}


def scrape_conversion_data(lst, unit_type):
    conversion_dict = {}
    permutations = itertools.permutations(lst, 2)
    for permutation in permutations:
        i, j = permutation
        driver.implicitly_wait(5)
        if i not in conversion_dict:
            conversion_dict[i] = {}
        print(i, j)
        time.sleep(3)
        # because the scraper will move too fast so google will think its a robot making queries
        driver.get(str(f"https://www.google.com/search?q=convert+{i}+to+{j}"))
        # uses google search query
        conversion_string = driver.find_element(By.CLASS_NAME, "bjhkR").text.split(" ")
        # finds the div with this classname to return the conversion description

        name = "to_" + j
        conversion_dict[i][name] = {}
        if "e+" in conversion_string[-1]:
            conversion_num_placeholder = conversion_string[-1].split("e+")
            conversion_num = float(
                conversion_num_placeholder[0].replace(",", ".")
            ) * 10 ** int(conversion_num_placeholder[-1])
            conversion_dict[i][name]["conversion_num"] = float(conversion_num)
        elif "e+" not in conversion_string[-1]:
            conversion_dict[i][name]["conversion_num"] = float(
                conversion_string[-1].replace(",", ".")
            )

        # google will use local language with the same URL. Potential bug here.
        if "multiply" in conversion_string or "multiplier" in conversion_string:
            conversion_dict[i][name]["operation"] = "multiply"
        elif "divide" in conversion_string or "diviser" in conversion_string:
            conversion_dict[i][name]["operation"] = "divide"

    with open(f"units/{unit_type}.py", "w") as fp:
        json.dump(conversion_dict, fp, indent=4)


scrape_conversion_data(unit_dict["pressure"], "pressure")
