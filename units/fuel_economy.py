def convert(starting_unit,num): #function for working with converting units with equations
    data = {}
    for i in fuel_data[starting_unit].items():
        #_print(i[1])
        unit_name = i[0]
        unit_data = i[1]
        if len(unit_data) == 3: #this is needed because some unit conversions require equtions with different or_multiple steps
            #_print(i[1]["function"])
            data[f"to_{unit_name}"] = unit_data["conversion_num"] / num

        elif len(unit_data) == 2: #if the converted unit is normal and doesnt require a function
            #_print(i)
            if unit_data["operation"] == "multiply":
                data[unit_name] = num * unit_data["conversion_num"]
                # return name,original_num * data["conversion_num"]
            
            elif unit_data["operation"] == "divide":
                data[unit_name] = num / unit_data["conversion_num"]
                # return name,original_num / data["conversion_num"]
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
            "function":convert
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
            "function":convert
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
            "function":convert
        }
    },
    "Liter_per_100_kilometers":{
        "Miles_per_gallon":{
            "conversion_num": 235.215,
            "operation": "divide",
            "function":convert
        },
        "Kilometer_per_liter":{
            "conversion_num": 100,
            "operation": "divide",
            "function":convert
        },
        "Miles_per_gallon_(Imperial)":{
            "conversion_num": 282.481,
            "operation": "divide",
            "function":convert
        }
    }
}

#_print(convert("Liter_per_100 kilometers",89))