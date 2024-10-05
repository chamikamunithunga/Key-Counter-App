from flask import Flask, render_template, jsonify
from pynput import keyboard
import threading

app = Flask(__name__)
key_count = 0

def on_press(key):
    global key_count
    key_count += 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_count')
def get_count():
    return jsonify({'count': key_count})

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()
    app.run(debug=True, port=5001) 
