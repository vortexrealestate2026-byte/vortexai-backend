import psycopg2
import os


def get_connection():

    conn = psycopg2.connect(
        os.getenv("DATABASE_URL")
    )

    return conn
