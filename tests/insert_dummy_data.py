import sqlite3
import json

# Koneksi ke database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

import sqlite3
import json

# ... (Koneksi database sama seperti sebelumnya)

# === Perbaikan & Penambahan Tabel Gejala ===
cursor.execute("DROP TABLE IF EXISTS symptoms")  # Hapus tabel lama untuk direstrukturisasi
cursor.execute("""
CREATE TABLE symptoms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    medical_term TEXT,  # Istilah medis resmi
    severity INTEGER CHECK(severity BETWEEN 1 AND 3),  # Tingkat keparahan (1: ringan, 3: parah)
    body_part TEXT DEFAULT 'wajah',
    image TEXT
)
""")

# Gejala yang Diperbarui (+8 gejala baru)
symptoms_data = [
    ("Kulit Berminyak", "Seborrhea", 1, "wajah", "symptoms/oily_skin.jpg"),
    ("Papula Eritematosa", "Inflammatory Acne", 2, "wajah", "symptoms/red_acne.jpg"),
    ("Deskuamasi", "Scaling", 2, "wajah", "symptoms/scaly_skin.jpg"),
    ("Eritema", "Erythema", 2, "wajah", "symptoms/red_rash.jpg"),
    ("Xerosis", "Xerosis cutis", 2, "wajah", "symptoms/dry_skin.jpg"),
    ("Pruritus", "Pruritus", 3, "wajah", "symptoms/itchy_skin.jpg"),
    ("Hiperpigmentasi", "Post-inflammatory hyperpigmentation", 1, "wajah", "symptoms/dark_spots.jpg"),
    ("Komedo Terbuka", "Open comedones", 1, "wajah", "symptoms/large_pores.jpg"),
    ("Milium", "Milia", 1, "wajah", "symptoms/milia.jpg"),
    ("Nodul", "Nodulocystic Acne", 3, "wajah", "symptoms/cystic_acne.jpg"),
    ("Likenifikasi", "Lichenification", 3, "wajah", "symptoms/lichenification.jpg"),
    ("Pustula", "Pustule", 2, "wajah", "symptoms/pustule.jpg"),
    ("Ekskoriasi", "Excoriation", 2, "wajah", "symptoms/excoriation.jpg"),
    ("Skuama Keperakan", "Silvery Scale", 2, "wajah", "symptoms/silvery_scale.jpg"),
    ("Telangiektasia", "Telangiectasia", 1, "wajah", "symptoms/telangiectasia.jpg")
]
cursor.executemany("INSERT INTO symptoms (name, medical_term, severity, body_part, image) VALUES (?,?,?,?,?)", symptoms_data)

# === Penyakit dengan Bobot Terupdate ===
diseases_data = [
    {   # Jerawat (Versi Lebih Detil)
        "name": "Akne Vulgaris",
        "required_symptoms": json.dumps([1,2,7,10]),  # ID gejala
        "weighted_symptoms": json.dumps({
            "1": 0.3,  # Kulit berminyak
            "2": 0.5,  # Papula
            "7": 0.1,  # Hiperpigmentasi
            "10": 0.6   # Nodul
        }),
        "description": "Kelainan folikel pilosebasea dengan manifestasi komedo, papul, pustul, dan nodul.",
        "skincare": json.dumps(["Retinoid Topikal", "Antibiotik Topikal", "Benzoil Peroksida"]),
        "disease_image": "diseases/acne_vulgaris.jpg"
    },
    {   # Eksim (Dermatitis Atopik)
        "name": "Dermatitis Atopik",
        "required_symptoms": json.dumps([4,5,6,11]),
        "weighted_symptoms": json.dumps({
            "4": 0.4,  # Eritema
            "5": 0.5,  # Xerosis
            "6": 0.7,  # Pruritus
            "11": 0.3   # Likenifikasi
        }),
        "description": "Peradangan kronis dengan gejala gatal hebat, kulit kering, dan likenifikasi.",
        "skincare": json.dumps(["Emolien", "Kortikosteroid Topikal", "Inhibitor Kalsineurin"]),
        "disease_image": "diseases/atopic_dermatitis.jpg"
    },
    {   # Psoriasis
        "name": "Psoriasis Vulgaris",
        "required_symptoms": json.dumps([3,13,14]),
        "weighted_symptoms": json.dumps({
            "3": 0.4,   # Deskuamasi
            "13": 0.8,  # Skuama Keperakan
            "14": 0.2   # Telangiektasia
        }),
        "description": "Proliferasi keratinosit yang cepat dengan plak eritematosa berskuama tebal.",
        "skincare": json.dumps(["Analog Vitamin D3", "Kortikosteroid Potensi Tinggi", "Terapi Sinar UVB"]),
        "disease_image": "diseases/psoriasis_vulgaris.jpg"
    },
    {   # Rosacea (Penyakit Baru)
        "name": "Rosacea",
        "required_symptoms": json.dumps([4,12,14]),
        "weighted_symptoms": json.dumps({
            "4": 0.6,   # Eritema
            "12": 0.5,  # Telangiektasia
            "14": 0.4   # Pustula
        }),
        "description": "Vaskulopati kronis dengan eritema sentrofasial, telangiektasia, dan papulopustula.",
        "skincare": json.dumps(["Metronidazole Topikal", "Ivermectin Topikal", "Proteksi Sinar Matahari"]),
        "disease_image": "diseases/rosacea.jpg"
    }
]

# ... (Proses insert data penyakit dan skincare tetap sama, dengan penambahan data baru)

# === Skincare yang Diperbarui ===
skincare_data = [
    # ... (Data sebelumnya),
    ("Retinoid Topikal", "Anti-inflamasi & Regenerasi", "skincare/retinoid.jpg"),
    ("Inhibitor Kalsineurin", "Imunomodulator", "skincare/tacrolimus.jpg"),
    ("Terapi Sinar UVB", "Fototerapi", "skincare/uvb_therapy.jpg"),
    ("Ivermectin Topikal", "Anti-parasit", "skincare/ivermectin.jpg")
]

# ... (Commit dan close connection)






# Simpan perubahan
target_commit = conn.commit()
if target_commit is None:
    print("✅ Database telah dibuat dan diisi dengan data skincare Skintific!")
conn.close()