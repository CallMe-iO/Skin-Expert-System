import sqlite3
import json

# Fungsi Forward Chaining murni (IF-THEN)
def forward_chaining(selected_symptoms):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM diseases")
    diseases = cursor.fetchall()
    conn.close()

    for disease in diseases:
        disease_id, name, required_symptoms, weighted_symptoms, description, skincare, _ = disease
        required_symptoms = json.loads(required_symptoms)  # Gejala wajib
        
        # Jika semua gejala wajib ada dalam input user, maka cocok
        if all(str(symptom) in selected_symptoms for symptom in required_symptoms):
            return {
                "penyakit": name,
                "deskripsi": description,
                "skincare": json.loads(skincare)  # Rekomendasi skincare
            }
    
    return None  # Tidak ada penyakit yang cocok

# Fungsi Forward Chaining dengan Bobot
def forward_chaining_weighted(selected_symptoms):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM diseases")
    diseases = cursor.fetchall()
    conn.close()

    best_match = None
    highest_score = 0

    for disease in diseases:
        disease_id, name, required_symptoms, weighted_symptoms, description, skincare, _ = disease
        required_symptoms = json.loads(required_symptoms)
        weighted_symptoms = json.loads(weighted_symptoms)

        # Hitung skor berdasarkan gejala yang dipilih
        score = sum(float(weighted_symptoms.get(str(symptom), 0)) for symptom in selected_symptoms)

        if score > highest_score:
            highest_score = score
            best_match = {
                "penyakit": name,
                "deskripsi": description,
                "skincare": json.loads(skincare),
                "skor": highest_score
            }
    
    return best_match if best_match else None
