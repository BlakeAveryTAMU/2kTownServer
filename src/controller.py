from src import queries
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
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


def add_user(email, password, team_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    print(email + " " + password + " " + team_id)

    try:
        cursor.execute(queries.add_user, (email, password, team_id))
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()