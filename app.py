from flask import Flask, request, render_template
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.environ["DB_HOST"],
    "port": int(os.environ.get("DB_PORT")),
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "database": os.environ["DB_NAME"]

}

def get_db():
    return mysql.connector.connect(**db_config)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO messages (content) VALUES (%s)",
            (message,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    # Fetch messages
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT content, created_at FROM messages ORDER BY created_at DESC"
    )
    messages = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
