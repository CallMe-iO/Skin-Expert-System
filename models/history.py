import sqlite3
import json

def save_diagnosis(user_id, selected_symptoms, disease, score, skincare):
    if user_id is None:
        return False  # Pastikan user login sebelum menyimpan

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history (user_id, symptoms, disease, score, skincare) 
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, json.dumps(selected_symptoms), disease, score, json.dumps(skincare)))

    conn.commit()
    conn.close()
    return True
