from flask import Flask, render_template,request,session,redirect
from dotenv import load_dotenv
from flask_socketio import SocketIO,emit
from length import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'create secret later'
socketio = SocketIO(app)


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

@app.route("/")
def home():
    return render_template("home.html")

@socketio.on('originalMillimeter')
def handle_message(data):
    print(data)
    dict = {}
    for conversion_type in length[data["originalConversion"]].items(): #loop through all of millimeters dict to call the function to convert new desired type
        # print(conversion_type)
        name = conversion_type[0]
        func = conversion_type[1]
        dict[name] = length[data["originalConversion"]][conversion_type[0]](90) #creates entry in dictionary stating new conversion type as the name and the value will be the function called 

    print(dict)
    emit('new_data',dict)



if __name__ == '__main__':
    socketio.run(app,debug=True,port=8000)
