from flask import Flask, render_template,request,session,redirect
from dotenv import load_dotenv
from flask_socketio import SocketIO,emit
import units #needed to import everything in the __init__.py file in the units folder

app = Flask(__name__)
app.config['SECRET_KEY'] = 'create secret later'
socketio = SocketIO(app)

UNITS = {
    "length":units.length_data,
    "speed":units.speed_data,
    "volume":units.volume_data,
    "mass":units.mass_data,
    "pressure":units.pressure_data,
    "frequency":units.frequency_data,
    "energy":units.energy_data,
    "time":units.time_data,
    "fuel":units.fuel_data,
    "temperature":units.temperature_data
}

@app.route("/")
def home():
    return render_template("home.html")

@socketio.on('originalToConvert')
def handle_message(socket_data:dict): #better than making 100 different functions for every conversion type also rounds to the 5th decimal place
    print(socket_data)
    converted_data = {}
    for original_type in UNITS[socket_data["unit"]][socket_data["originalConversion"]].items(): #indexes the dictionary to return the unit values
        # print(original_type)
        name = original_type[0].replace("to_","").replace("_"," ") #returns the name of the unit currently being converted
        original_data = original_type[1] 
        if len(original_data) == 3: #this is needed because some unit conversions require equtions with different or multiple steps
            # print(socket_data)
            print(original_data)
            converted_data.update(original_data["function"](socket_data["originalConversion"],float(socket_data["originalNumber"]))) #the original_data["function"] calls the function inside the selected unit dict by passing the params of the original starting unit and the original number to be converted and then this is calculated in another file which is put inside a dict then the dict is then joined together with the dict here

        elif len(original_data) == 2: #if the converted unit is normal and doesnt require a function
            if original_data["operation"] == "multiply":
                converted_data[name] = round(float(socket_data["originalNumber"]) * original_data["conversion_num"],5)
            
            elif original_data["operation"] == "divide":
                converted_data[name] = round(float(socket_data["originalNumber"]) / original_data["conversion_num"],5)

    print(converted_data)
    # return converted_data
    emit('new_data',converted_data) #sends data to frontend

@socketio.on('getUnitKeys')
def get_unit_keys(socket_data:dict): #needed to get unit measurements of selected unit requested from frontend
    print(UNITS[socket_data["unit"]].keys())
    emit('unit_keys',{"key_names":list(UNITS[socket_data["unit"]].keys())}) #sends a list of measurements names of the desired unit requested from frontend
    return UNITS[socket_data["unit"]].keys()


if __name__ == '__main__':
    socketio.run(app,debug=True,port=8000)

