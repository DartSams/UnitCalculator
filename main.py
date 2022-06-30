from flask import Flask, render_template,request,session,redirect
from dotenv import load_dotenv
from flask_socketio import SocketIO,emit
from length import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'create secret later'
socketio = SocketIO(app)


@app.route("/")
def home():
    return render_template("home.html")

@socketio.on('original')
def handle_message(socket_data):
    print(socket_data)
    converted_data = {}
    for original_type in length_data[socket_data["originalConversion"]].items():
        name = original_type[0]
        original_data = original_type[1]
        if original_data["operation"] == "multiply":
            converted_data[name] = float(socket_data["originalNumber"]) * original_data["conversion_num"]
        
        elif original_data["operation"] == "divide":
            converted_data[name] = float(socket_data["originalNumber"]) / original_data["conversion_num"]

    # return converted_data
    emit('new_data',converted_data) #sends data to frontend



if __name__ == '__main__':
    socketio.run(app,debug=True,port=8000)
