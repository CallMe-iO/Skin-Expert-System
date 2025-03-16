from models.database import get_all, get_by_id
import json

def calculate_disease_probability(selected_symptoms):
    """
    Menghitung probabilitas penyakit berdasarkan:
    - Gejala wajib (required_symptoms)
    - Gejala tambahan dengan bobot (weighted_symptoms)
    """
    diseases = get_all('diseases')
    results = []

    for disease in diseases:
        # Parse data dari database
        required = json.loads(disease['required_symptoms'])
        weighted = json.loads(disease['weighted_symptoms'])
        
        # Step 1: Cek gejala wajib
        if not all(symptom in selected_symptoms for symptom in required):
            continue  # Lewat jika gejala wajib tidak terpenuhi
        
        # Step 2: Hitung skor bobot
        score = 0
        for symptom_id in selected_symptoms:
            score += weighted.get(str(symptom_id), 0)
        
        # Step 3: Normalisasi skor
        max_score = sum(weighted.values())
        probability = (score / max_score) * 100 if max_score > 0 else 0

        results.append({
            'disease': disease,
            'probability': round(probability, 2)
        })

    # Urutkan berdasarkan probabilitas tertinggi
    return sorted(results, key=lambda x: x['probability'], reverse=True)