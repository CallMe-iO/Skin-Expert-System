from models.logic import diagnose

# Contoh input: User memilih gejala dengan ID 1 dan 2
selected_symptoms = [1, 2]

# Jalankan diagnosa
result = diagnose(selected_symptoms)

# Tampilkan hasil
if result:
    disease_name, score, skincare = result[0]
    print(f"Diagnosis: {disease_name} (Skor: {score:.2f})")
    print("Rekomendasi Skincare:", ", ".join(skincare))
else:
    print("Tidak ada penyakit yang cocok.")
