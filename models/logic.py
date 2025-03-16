import sqlite3
import json

def diagnose(selected_symptoms):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Ambil data penyakit
    cursor.execute("SELECT id, name, required_symptoms, weighted_symptoms, skincare FROM diseases")
    diseases = cursor.fetchall()

    diagnosis_result = []

    for disease in diseases:
        disease_id, name, required_symptoms, weighted_symptoms, skincare = disease

        required_symptoms = json.loads(required_symptoms)  # Convert JSON string to list
        weighted_symptoms = json.loads(weighted_symptoms)  # Convert JSON string to dict
        skincare = json.loads(skincare)  # Convert JSON string to list

        # Cek apakah semua gejala wajib dipenuhi
        if not all(symptom in selected_symptoms for symptom in required_symptoms):
            continue  # Skip penyakit ini kalau gejala wajibnya tidak terpenuhi

        # Hitung skor kecocokan berdasarkan bobot gejala
        score = sum(weighted_symptoms.get(str(symptom), 0) for symptom in selected_symptoms)

        # Simpan hasil diagnosa
        diagnosis_result.append((name, score, skincare))

    conn.close()

    # Urutkan hasil berdasarkan skor tertinggi
    diagnosis_result.sort(key=lambda x: x[1], reverse=True)

    return diagnosis_result[:1]  # Ambil hasil dengan skor tertinggi
