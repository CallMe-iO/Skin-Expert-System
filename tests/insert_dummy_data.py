import sqlite3
import json

# Koneksi ke database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# === Buat Tabel ===

# Tabel Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT CHECK(role IN ('user', 'admin')) NOT NULL
)
""")

# Tabel Gejala
cursor.execute("""
CREATE TABLE IF NOT EXISTS symptoms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    image TEXT
)
""")

# Tabel Penyakit
cursor.execute("""
CREATE TABLE IF NOT EXISTS diseases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    required_symptoms TEXT,  -- JSON array
    weighted_symptoms TEXT,   -- JSON object
    description TEXT,
    skincare TEXT,
    disease_image TEXT
)
""")

# Tabel Rekomendasi Skincare
cursor.execute("""
CREATE TABLE IF NOT EXISTS skincare (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    image TEXT
)
""")

# Tabel Riwayat Diagnosa
cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER, 
    symptoms TEXT,
    disease TEXT,
    score REAL,
    skincare TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

# === Tambah Data Dummy ===

# Data Dummy User
cursor.executemany("""
INSERT INTO users (username, password, role) VALUES (?, ?, ?)
""", [
    ("admin", "admin123", "admin"),
    ("user1", "password1", "user"),
    ("user2", "password2", "user")
])

# Data Dummy Gejala
cursor.executemany("""
INSERT INTO symptoms (name, image) VALUES (?, ?)
""", [
    ("Kulit Berminyak", "symptoms/oily_skin.jpg"),
    ("Jerawat Merah", "symptoms/red_acne.jpg"),
    ("Kulit Bersisik", "symptoms/scaly_skin.jpg"),
    ("Ruam Kemerahan", "symptoms/red_rash.jpg"),
    ("Kulit Kering", "symptoms/dry_skin.jpg")
])

# Data Dummy Penyakit
diseases_data = [
    {
        "name": "Jerawat",
        "required_symptoms": json.dumps([1, 2]),
        "weighted_symptoms": json.dumps({"1": 0.6, "2": 0.4}),
        "description": "Penyakit kulit akibat pori-pori tersumbat oleh minyak dan sel kulit mati.",
        "skincare": json.dumps(["Salicylic Acid", "Benzoyl Peroxide"]),
        "disease_image": "diseases/acne.jpg"
    },
    {
        "name": "Dermatitis",
        "required_symptoms": json.dumps([3, 4]),
        "weighted_symptoms": json.dumps({"3": 0.5, "4": 0.5}),
        "description": "Peradangan kulit yang menyebabkan ruam merah, gatal, dan bersisik.",
        "skincare": json.dumps(["Moisturizer", "Hydrocortisone Cream"]),
        "disease_image": "diseases/dermatitis.jpg"
    },
    {
        "name": "Psoriasis",
        "required_symptoms": json.dumps([3, 5]),
        "weighted_symptoms": json.dumps({"3": 0.7, "5": 0.3}),
        "description": "Penyakit autoimun yang menyebabkan kulit bersisik dan bercak merah.",
        "skincare": json.dumps(["Coal Tar Shampoo", "Steroid Cream"]),
        "disease_image": "diseases/psoriasis.jpg"
    }
]

for disease in diseases_data:
    cursor.execute("""
    INSERT INTO diseases (name, required_symptoms, weighted_symptoms, description, skincare, disease_image) 
    VALUES (?, ?, ?, ?, ?, ?)
    """, (disease["name"], disease["required_symptoms"], disease["weighted_symptoms"], disease["description"], disease["skincare"], disease["disease_image"]))

# Data Dummy Skincare
cursor.executemany("""
INSERT INTO skincare (name, type, image) VALUES (?, ?, ?)
""", [
    ("Salicylic Acid", "Acne Treatment", "skincare/salicylic_acid.jpg"),
    ("Benzoyl Peroxide", "Acne Treatment", "skincare/benzoyl_peroxide.jpg"),
    ("Moisturizer", "Hydration", "skincare/moisturizer.jpg"),
    ("Hydrocortisone Cream", "Anti-Inflammatory", "skincare/hydrocortisone.jpg"),
    ("Coal Tar Shampoo", "Psoriasis Treatment", "skincare/coal_tar.jpg"),
    ("Steroid Cream", "Psoriasis Treatment", "skincare/steroid_cream.jpg")
])

# Data Dummy Riwayat Diagnosa
cursor.executemany("""
INSERT INTO history (user_id, symptoms, disease, score, skincare) VALUES (?, ?, ?, ?, ?)
""", [
    (1, json.dumps([1, 2]), "Jerawat", 0.60, json.dumps(["Salicylic Acid", "Benzoyl Peroxide"])),
    (2, json.dumps([3, 4]), "Dermatitis", 0.50, json.dumps(["Moisturizer", "Hydrocortisone Cream"])),
    (1, json.dumps([3, 5]), "Psoriasis", 0.70, json.dumps(["Coal Tar Shampoo", "Steroid Cream"]))
])

# Simpan perubahan
conn.commit()
conn.close()

print("✅ Database telah dibuat dan diisi dengan data dummy!")
