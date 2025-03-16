import sqlite3

def get_symptoms():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM symptoms")  # Ambil gejala dari tabel symptoms
    symptoms = {str(row[0]): row[1] for row in cursor.fetchall()}  # ID tetap string

    conn.close()
    return symptoms
