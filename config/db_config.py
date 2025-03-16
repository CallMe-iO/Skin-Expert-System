import os
import sqlite3

# Path ke database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, '../../database.db')

def get_db_connection():
    return sqlite3.connect(DATABASE_PATH)