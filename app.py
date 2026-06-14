from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "sql_container",   # matches container name
    "user": "root",
    "password": "rootpassword",
    "database": "testdb"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["username"]
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
        cursor.close()
        conn.close()
        return f"Hello {name}, saved!"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000 )

