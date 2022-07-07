def fuel_convert(starting_unit:str,num:float): #function for working with fuel_converting units with equations
    data = {}
    for i in fuel_data[starting_unit].items():
        #_print(i[1])
        unit_name = i[0]
        unit_data = i[1]
        if len(unit_data) == 3: #this is needed because some unit conversions require equtions with different or_multiple steps
            #_print(i[1]["function"])
            # data[f"answer"] = unit_data["conversion_num"] / num ####works
            # return unit_data["conversion_num"] / num ####works
            data[f"{unit_name}"] = unit_data["conversion_num"] / num ####works

    return data


fuel_data = {
    "Miles_per_gallon":{
        "Miles_per_gallon_(Imperial)":{
            "conversion_num": 1.201,
            "operation": "multiply",
        },
        "Kilometer_per_liter":{
            "conversion_num": 2.352,
            "operation": "divide"
        },
        "Liter_per_100_kilometers":{
            "conversion_num": 235.215,
            "operation": "divide",
            "function":fuel_convert
        },
    },
    "Miles_per_gallon_(Imperial)":{
        "Miles_per_gallon":{
            "conversion_num": 1.201,
            "operation": "divide"
        },
        "Kilometer_per_liter":{
            "conversion_num": 2.825,
            "operation": "divide"
        },
        "Liter_per_100_kilometers":{
            "conversion_num": 282.481,
            "operation": "divide",
            "function":fuel_convert
        },
    },
    "Kilometer_per_liter":{
        "Miles_per_gallon":{
            "conversion_num": 2.352,
            "operation": "multiply",
        },
        "Miles_per_gallon_(Imperial)":{
            "conversion_num": 2.825,
            "operation": "multiply",
        },
        "Liter_per_100_kilomers":{
            "conversion_num": 100,
            "operation": "divide",
            "function":fuel_convert
        }
    },
    "Liter_per_100_kilometers":{
        "Miles_per_gallon":{
            "conversion_num": 235.215,
            "operation": "divide",
            "function":fuel_convert
        },
        "Kilometer_per_liter":{
            "conversion_num": 100,
            "operation": "divide",
            "function":fuel_convert
        },
        "Miles_per_gallon_(Imperial)":{
            "conversion_num": 282.481,
            "operation": "divide",
            "function":fuel_convert
        }
    }
}

# print(fuel_convert("Miles_per_gallon",89))