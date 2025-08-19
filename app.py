from flask import Flask, request, jsonify, render_template
import mysql.connector
import os

app = Flask(__name__)

# MySQL config from env vars
DB_HOST = os.environ.get("DB_HOST", "mysql_db")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "rootpass")
DB_NAME = os.environ.get("DB_NAME", "flaskdb")

def get_db_connection():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn

@app.route("/", methods=["GET"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM messages ORDER BY id DESC")
    messages = cursor.fetchall()
    conn.close()
    return render_template("index.html", messages=messages)

@app.route("/submit", methods=["POST"])
def submit():
    message = request.form.get("new_message")
    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
    conn.commit()
    conn.close()

    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

