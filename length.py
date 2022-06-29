def mm_to_centimeter(mm_num):
    return mm_num/10

def mm_to_inch(mm_num):
    return mm_num/25.4

def mm_to_feet(mm_num):
    return mm_num/304.8

def mm_to_yard(mm_num):
    return mm_num/914.4

def mm_to_meter(mm_num):
    return mm_num/1000

def mm_to_kilometer(mm_num):
    return mm_num/1*10**6

def mm_to_miles(mm_num):
    return mm_num/1.609*10**6

##************************************************8
def cm_to_milimeter(cm_num):
    return cm_num*10

def cm_to_inch(cm_num):
    return cm_num/2.54

def cm_to_feet(cm_num):
    return cm_num/30.48

def cm_to_yard(cm_num):
    return cm_num/91.44

def cm_to_meter(cm_num):
    return cm_num/100

def cm_to_kilometer(cm_num):
    return cm_num/100000

def cm_to_miles(cm_num):
    return cm_num/160900


##************************************************8
def cm_to_millimeter(cm_num):
    return cm_num*10

def cm_to_inch(cm_num):
    return cm_num/2.54

def cm_to_feet(cm_num):
    return cm_num/30.48

def cm_to_yard(cm_num):
    return cm_num/91.44

def cm_to_meter(cm_num):
    return cm_num/100

def cm_to_kilometer(cm_num):
    return cm_num/100000

def cm_to_miles(cm_num):
    return cm_num/160900

##************************************************8
def inch_to_milimeter(inch_num):
    return inch_num/25.4

def inch_to_centimeter(inch_num):
    return inch_num/2.54

def inch_to_feet(inch_num):
    return inch_num/12

def inch_to_yard(inch_num):
    return inch_num/36

def inch_to_meter(inch_num):
    return inch_num/39.37

def inch_to_kilometer(inch_num):
    return inch_num/39370

def inch_to_miles(inch_num):
    return inch_num/63360

##************************************************8
def feet_to_milimeter(feet_num):
    return feet_num*304.8

def feet_to_centimeter(feet_num):
    return feet_num*30.48

def feet_to_inch(feet_num):
    return feet_num*12

def feet_to_yard(feet_num):
    return feet_num/3

def feet_to_meter(feet_num):
    return feet_num/3.281

def feet_to_kilometer(feet_num):
    return feet_num/3281

def feet_to_miles(feet_num):
    return feet_num/5280

##************************************************8
def yard_to_milimeter(yard_num):
    return yard_num*914.4

def yard_to_centimeter(yard_num):
    return yard_num*91.44

def yard_to_inch(yard_num):
    return yard_num*36

def yard_to_feet(yard_num):
    return yard_num*3

def yard_to_meter(yard_num):
    return yard_num/1.094

def yard_to_kilometer(yard_num):
    return yard_num/1094

def yard_to_miles(yard_num):
    return yard_num/1760

##************************************************8
def meter_to_milimeter(meter_num):
    return meter_num*1000

def meter_to_centimeter(meter_num):
    return meter_num*100

def meter_to_inch(meter_num):
    return meter_num*39.37

def meter_to_feet(meter_num):
    return meter_num*3.281

def meter_to_yard(meter_num):
    return meter_num*1.094

def meter_to_kilometer(meter_num):
    return meter_num/1000

def meter_to_miles(meter_num):
    return meter_num/1609

##************************************************8
def kilometer_to_milimeter(kilometer_num):
    return kilometer_num*1*10**6

def kilometer_to_centimeter(kilometer_num):
    return kilometer_num*100000

def kilometer_to_inch(kilometer_num):
    return kilometer_num*39370

def kilometer_to_feet(kilometer_num):
    return kilometer_num*3281

def kilometer_to_yard(kilometer_num):
    return kilometer_num/1094

def kilometer_to_meter(kilometer_num):
    return kilometer_num*1000

def kilometer_to_miles(kilometer_num):
    return kilometer_num/1.609

##************************************************8
def mile_to_milimeter(mile_num):
    return mile_num*1.609*10**6

def mile_to_centimeter(mile_num):
    return mile_num*160900

def mile_to_inch(mile_num):
    return mile_num*63360

def mile_to_feet(mile_num):
    return mile_num*5280

def mile_to_yard(mile_num):
    return mile_num/1760

def mile_to_meter(mile_num):
    return mile_num*1609

def mile_to_kilometer(mile_num):
    return mile_num*1.609

length = {
    'millimeters':{
        'to_centimeter': mm_to_centimeter, #divide mm by 10
        'to_inch':mm_to_inch,
        'to_feet':mm_to_feet,
        'to_yard':mm_to_yard,
        'to_meter':mm_to_meter,
        'to_kilometer':mm_to_kilometer,
        'to_miles':mm_to_miles
    },
    'centimeters':{
        'to_millimeter': cm_to_milimeter, #multiply mm by 10
        'to_inch':cm_to_inch,
        'to_feet':cm_to_feet,
        'to_yard':cm_to_yard,
        'to_meter':cm_to_meter,
        'to_kilometer':cm_to_kilometer,
        'to_miles':cm_to_miles
    },
    'inches':{
        'to_millimeter': inch_to_milimeter, #multiply mm by 10
        'to_centimeter':inch_to_centimeter,
        'to_feet':inch_to_feet,
        'to_yard':inch_to_yard,
        'to_meter':inch_to_meter,
        'to_kilometer':inch_to_kilometer,
        'to_miles':inch_to_miles
    },
    'feet':{
        'to_millimeter': feet_to_milimeter, #multiply mm by 10
        'to_centimeter':feet_to_centimeter,
        'to_inch':feet_to_inch,
        'to_yard':feet_to_yard,
        'to_meter':feet_to_meter,
        'to_kilometer':feet_to_kilometer,
        'to_miles':feet_to_miles
    },
    'yard':{
        'to_millimeter': yard_to_milimeter, #multiply mm by 10
        'to_centimeter':yard_to_centimeter,
        'to_inch':yard_to_inch,
        'to_feet':yard_to_feet,
        'to_meter':yard_to_meter,
        'to_kilometer':yard_to_kilometer,
        'to_miles':yard_to_miles
    },
    'meter':{
        'to_millimeter': meter_to_milimeter, #multiply mm by 10
        'to_centimeter':meter_to_centimeter,
        'to_inch':meter_to_inch,
        'to_feet':meter_to_feet,
        'to_meter':meter_to_yard,
        'to_kilometer':meter_to_kilometer,
        'to_miles':meter_to_miles
    },
    'kilometer':{
        'to_millimeter': kilometer_to_milimeter, #multiply mm by 10
        'to_centimeter':kilometer_to_centimeter,
        'to_inch':kilometer_to_inch,
        'to_feet':kilometer_to_feet,
        'to_meter':kilometer_to_yard,
        'to_kilometer':kilometer_to_meter,
        'to_miles':kilometer_to_miles
    },
    'miles':{
        'to_millimeter': mile_to_milimeter, #multiply mm by 10
        'to_centimeter':mile_to_centimeter,
        'to_inch':mile_to_inch,
        'to_feet':mile_to_feet,
        'to_meter':mile_to_yard,
        'to_kilometer':mile_to_meter,
        'to_miles':mile_to_kilometer
    }
}

# for original_type in length.items(): #this level will return all conversion types
#     print(f"############{original_type[0]}############")
#     for conversion_type in length[original_type[0]].items(): #loop through all of the conversion types to call the function to convert new desired type
#         name = conversion_type[0]
#         func = conversion_type[1]
#         print(f"conversion:{name}-----{length[original_type[0]][name](90)}")


# for conversion_type in length['millimeters'].items(): #loop through all of millimeters dict to call the function to convert new desired type
#     # print(conversion_type)
#     name = conversion_type[0]
#     func = conversion_type[1]
#     # print(conversion_type[0])
#     # print(length['millimeters'][conversion_type[0]](90))
#     print(length['millimeters'][name](90))