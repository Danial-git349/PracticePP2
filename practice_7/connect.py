import psycopg2
from practice_7.config import db_params

def get_connection():
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True
    return conn