def temp_convert(starting_unit:str,num:float): #function for working with temp_converting units with equations
    data = {}
    for i in temperature_data[starting_unit].items():
        #_print(i[1])
        unit_name = i[0]
        unit_data = i[1]
        if unit_data["function"]:
            print("here")
        # print(i)
        if starting_unit == "Fahrenheit":
            if unit_name == "Celsius":
                data[unit_name] = (num - 32) * 5/9

            if unit_name == "Kelvin":
                data[unit_name] = (num - 32) * 5/9 + 273.15

        elif starting_unit == "Celsius":
            if unit_name == "Fahrenheit":
                data[unit_name] = (num * 9/5) + 32

            if unit_name == "Kelvin":
                data[unit_name] = num + 273.15

        elif starting_unit == "Kelvin":
            if unit_name == "Celsius":
                data[unit_name] = num - 273.15

            if unit_name == "Fahrenheit":
                data[unit_name] = (num - 273.15) * 9/5 + 32

    return data


temperature_data = {
    "Fahrenheit":{
        "Celsius":{
            "conversion_num": 0,
            "operation": "divide",
            "function":temp_convert 
        },
        "Kelvin":{
            "conversion_num": 0,
            "operation": "divide",
            "function":temp_convert
        }
    },
    "Celsius":{
        "Fahrenheit":{
            "conversion_num": 0,
            "operation": "divide",
            "function":temp_convert 
        },
        "Kelvin":{
            "conversion_num": 0,
            "operation": "divide",
            "function":temp_convert
        }
    },
    "Kelvin":{
        "Celsius":{
            "conversion_num": 0,
            "operation": "divide",
            "function":temp_convert 
        },
        "Fahrenheit":{
            "conversion_num": 0,
            "operation": "divide",
            "function":temp_convert
        }
    }
}

# print(temp_convert("Kelvin",89))