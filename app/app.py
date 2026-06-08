from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "appdb"),
        user=os.environ.get("DB_USER", "user"),
        password=os.environ.get("DB_PASS", "password")
    )

@app.route("/")
def index():
    return "<h1>Flask + PostgreSQL + Nginx is working!</h1>"

@app.route("/db")
def db_check():
    try:
        conn = get_db()
        conn.close()
        return "<h1>✅ Database connection successful!</h1>"
    except Exception as e:
        return f"<h1>❌ DB Error: {e}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
