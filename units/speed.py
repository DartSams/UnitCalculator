speed_data = {
    "foot/minute":{
        "to_miles/hour":{
            "conversion_num":88,
            "operation":"divide"
        },
        "to_foot/second":{
            "conversion_num":60,
            "operation":"divide"
        },
        "to_meters/second":{
            "conversion_num":196.9,
            "operation":"divide"
        },
        "to_kilometers/hour":{
            "conversion_num":54.681,
            "operation":"divide"
        }
    },
    "miles/hour":{
        "to_foot/minute":{
            "conversion_num":88,
            "operation":"multiply"
        },
        "to_foot/second":{
            "conversion_num":1.467,
            "operation":"multiply"
        },
        "to_meters/second":{
            "conversion_num":2.237,
            "operation":"divide"
        },
        "to_kilometers/hour":{
            "conversion_num":1.609,
            "operation":"multiply"
        }
    },
    "foot/second":{
        "to_foot/minute":{
            "conversion_num":60,
            "operation":"multiply"
        },
        "to_miles/hour":{
            "conversion_num":1.467,
            "operation":"divide"
        },
        "to_meters/second":{
            "conversion_num":3.281,
            "operation":"divide"
        },
        "to_kilometers/hour":{
            "conversion_num":1.097,
            "operation":"multiply"
        }
    },
    "meters/second":{
        "to_miles/hour":{
            "conversion_num":2.237,
            "operation":"multiply"
        },
        "to_foot/second":{
            "conversion_num":3.281,
            "operation":"multiply"
        },
        "to_foot/minute":{
            "conversion_num":196.9,
            "operation":"multiply"
        },
        "to_kilometers/hour":{
            "conversion_num":3.6,
            "operation":"multiply"
        }
    },
    "kilometers/hour":{
        "to_miles/hour":{
            "conversion_num":1609,
            "operation":"divide"
        },
        "to_foot/second":{
            "conversion_num":1.097,
            "operation":"divide"
        },
        "to_meters/second":{
            "conversion_num":3.6,
            "operation":"divide"
        },
        "to_foot/minute":{
            "conversion_num":54.681,
            "operation":"multiply"
        }
    }
}
UNITS = {
    "speed":speed_data
}

def conversion(original_num:int,original_type:str):
    converted_data = {}
    UNITS[original_type]
    for original_type in UNITS[original_type].items():
        name = original_type[0]
        data = original_type[1]
        if data["operation"] == "multiply":
            converted_data[name] = original_num * data["conversion_num"]
            # return name,original_num * data["conversion_num"]
        
        elif data["operation"] == "divide":
            converted_data[name] = original_num / data["conversion_num"]
            # return name,original_num / data["conversion_num"]

    return converted_data




# print(conversion(90,"foot/minute"))
# print(UNITS["foot/minute"])