from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
import sqlite3

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def connect_db():
    return sqlite3.connect("bus.db")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login_page')
def login_page():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login success", "role": user[3]})
    else:
        return jsonify({"message": "Invalid credentials"})

@app.route('/driver')
def driver_page():
    return render_template("driver.html")

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO locations (bus_id, latitude, longitude) VALUES (?, ?, ?)",
        (data['bus_id'], data['latitude'], data['longitude'])
    )

    conn.commit()
    conn.close()

    socketio.emit('location_update', data)

    return jsonify({"message": "Location updated"})

if __name__ == '__main__':
    socketio.run(app, debug=True)