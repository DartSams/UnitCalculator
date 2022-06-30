length_data = {
    "millimeters":{
        "to_centimeters":{
            "conversion_num":10,
            "operation":"divide"
        },
        'to_inch':{
            "conversion_num":25.4,
            "operation":"divide"
        },
        'to_feet':{
            "conversion_num":304.8,
            "operation":"divide"
        },
        'to_yard':{
            "conversion_num":914.4,
            "operation":"divide"
        },
        'to_meter':{
            "conversion_num":1000,
            "operation":"divide"
        },
        'to_kilometer':{
            "conversion_num":1*10**6,
            "operation":"divide"
        },
        'to_miles':{
            "conversion_num":1.609*10**6,
            "operation":"divide"
        }
    },
    'centimeters':{
        'to_millimeter': {
            "conversion_num":10,
            "operation":"multiply"
        }, 
        'to_inch':{
            "conversion_num":2.54,
            "operation":"divide"
        },
        'to_feet':{
            "conversion_num":30.48,
            "operation":"divide"
        },
        'to_yard':{
            "conversion_num":91.44,
            "operation":"divide"
        },
        'to_meter':{
            "conversion_num":100,
            "operation":"divide"
        },
        'to_kilometer':{
            "conversion_num":100000,
            "operation":"divide"
        },
        'to_miles':{
            "conversion_num":160900,
            "operation":"divide"
        }
    },
    'inches':{
        'to_millimeter': {
            "conversion_num":25.4,
            "operation":"multiply"
        }, 
        'to_centimeter':{
            "conversion_num":2.54,
            "operation":"multiply"
        },
        'to_feet':{
            "conversion_num":12,
            "operation":"divide"
        },
        'to_yard':{
            "conversion_num":36,
            "operation":"divide"
        },
        'to_meter':{
            "conversion_num":39.37,
            "operation":"divide"
        },
        'to_kilometer':{
            "conversion_num":39370,
            "operation":"divide"
        },
        'to_miles':{
            "conversion_num":63360,
            "operation":"divide"
        }
    },
    'feet':{
        'to_millimeter': {
            "conversion_num":304.8,
            "operation":"multiply"
        }, 
        'to_centimeter':{
            "conversion_num":30.48,
            "operation":"multiply"
        },
        'to_inch':{
            "conversion_num":12,
            "operation":"multiply"
        },
        'to_yard':{
            "conversion_num":3,
            "operation":"divide"
        },
        'to_meter':{
            "conversion_num":3.281,
            "operation":"divide"
        },
        'to_kilometer':{
            "conversion_num":3281,
            "operation":"divide"
        },
        'to_miles':{
            "conversion_num":5280,
            "operation":"divide"
        }
    },
    'yard':{
        'to_millimeter': {
            "conversion_num":914.4,
            "operation":"multiply"
        }, 
        'to_centimeter':{
            "conversion_num":91.44,
            "operation":"multiply"
        },
        'to_inch':{
            "conversion_num":36,
            "operation":"multiply"
        },
        'to_feet':{
            "conversion_num":3,
            "operation":"multiply"
        },
        'to_meter':{
            "conversion_num":1.094,
            "operation":"divide"
        },
        'to_kilometer':{
            "conversion_num":1094,
            "operation":"divide"
        },
        'to_miles':{
            "conversion_num":1760,
            "operation":"divide"
        }
    },
    'meter':{
        'to_millimeter': {
            "conversion_num":1000,
            "operation":"multiply"
        }, 
        'to_centimeter':{
            "conversion_num":100,
            "operation":"multiply"
        },
        'to_inch':{
            "conversion_num":39.37,
            "operation":"multiply"
        },
        'to_feet':{
            "conversion_num":3.281,
            "operation":"multiply"
        },
        'to_yard':{
            "conversion_num":1.094,
            "operation":"multiply"
        },
        'to_kilometer':{
            "conversion_num":1000,
            "operation":"divide"
        },
        'to_miles':{
            "conversion_num":1609,
            "operation":"divide"
        }
    },
    'kilometer':{
        'to_millimeter': {
            "conversion_num":1*10**6,
            "operation":"multiply"
        }, 
        'to_centimeter':{
            "conversion_num":100000,
            "operation":"multiply"
        },
        'to_inch':{
            "conversion_num":39370,
            "operation":"multiply"
        },
        'to_feet':{
            "conversion_num":3281,
            "operation":"multiply"
        },
        'to_meter':{
            "conversion_num":1000,
            "operation":"multiply"
        },
        'to_yard':{
            "conversion_num":1094,
            "operation":"multiply"
        },
        'to_miles':{
            "conversion_num":1.609,
            "operation":"divide"
        }
    },
    'miles':{
        'to_millimeter': {
            "conversion_num":1.609*10**6,
            "operation":"multiply"
        }, 
        'to_centimeter':{
            "conversion_num":160900,
            "operation":"multiply"
        },
        'to_inch':{
            "conversion_num":63360,
            "operation":"multiply"
        },
        'to_feet':{
            "conversion_num":5280,
            "operation":"multiply"
        },
        'to_meter':{
            "conversion_num":1609,
            "operation":"multiply"
        },
        'to_kilometer':{
            "conversion_num":1.609,
            "operation":"multiply"
        },
        'to_yard':{
            "conversion_num":1760,
            "operation":"multiply"
        }
    }
}

def conversion(original_num:int,original_type:str):
    converted_data = {}
    for original_type in length_data[original_type].items():
        name = original_type[0]
        data = original_type[1]
        if data["operation"] == "multiply":
            converted_data[name] = original_num * data["conversion_num"]
            # return name,original_num * data["conversion_num"]
        
        elif data["operation"] == "divide":
            converted_data[name] = original_num / data["conversion_num"]
            # return name,original_num / data["conversion_num"]

    return converted_data


# print(conversion(90,'miles'))