from flask import Flask, render_template,request,session,redirect
from dotenv import load_dotenv
from flask_socketio import SocketIO,emit
from length import length_data
from speed import speed_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'create secret later'
socketio = SocketIO(app)

UNITS = {
    "length":length_data,
    "speed":speed_data
}

@app.route("/")
def home():
    return render_template("home.html")

@socketio.on('original')
def handle_message(socket_data:dict): #better than making 100 different functions for every conversion type also rounds to the 5th decimal place
    print(socket_data)
    converted_data = {}
    for original_type in UNITS[socket_data["unit"]][socket_data["originalConversion"]].items(): #indexes the dictionary to return the unit values
        name = original_type[0] #returns the name of the unit currently being converted
        original_data = original_type[1] 
        if original_data["operation"] == "multiply":
            converted_data[name] = round(float(socket_data["originalNumber"]) * original_data["conversion_num"],5)
        
        elif original_data["operation"] == "divide":
            converted_data[name] = round(float(socket_data["originalNumber"]) / original_data["conversion_num"],5)

    # return converted_data
    emit('new_data',converted_data) #sends data to frontend



if __name__ == '__main__':
    socketio.run(app,debug=True,port=8000)
