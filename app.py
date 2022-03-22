from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'
socketio = SocketIO(app)

@app.route("/")
def index():
    # Render HTML with count variable
    return render_template("index.html")

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

@socketio.on('appdata')
def mouseMessage(data):
    emit('update value', data, broadcast=True)
    print(data)
 
#@socketio.on('mouse')
#def mouseMessage(data):
 #   emit('my response', data, broadcast=True)
  #  print('position: ' + data)
  #  send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)
    #app.run()