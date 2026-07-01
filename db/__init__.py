import psycopg2
from dotenv import load_dotenv
import os

def get_connection():
    load_dotenv(dotenv_path=".env")
    connection = psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT")
    )
    return connection

if __name__ == "__main__":
    connection = get_connection()
    print("Connection successful")
    connection.close()

