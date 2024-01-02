from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Retrieve database connection parameters from environment variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

def get_db_connection():
    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    return conn

@app.route("/api/")
def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)