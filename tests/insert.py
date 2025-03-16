import sqlite3
import json

# Koneksi ke database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
