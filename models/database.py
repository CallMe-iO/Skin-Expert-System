import sqlite3

def get_symptoms():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM symptoms")  # Ambil gejala dari tabel symptoms
    symptoms = {str(row[0]): row[1] for row in cursor.fetchall()}  # ID tetap string

    conn.close()
    return symptoms

def get_skincare_info(skincare_name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, type, image FROM skincare WHERE name = ?", (skincare_name,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {"name": row[0], "type": row[1], "image": row[2]}
    return None