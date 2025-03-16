import sqlite3

def create_database():
    conn = sqlite3.connect("database.db")  # Buat / koneksi ke database
    cursor = conn.cursor()

    # Tabel penyakit
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diseases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        required_symptoms TEXT,  -- JSON array (gejala wajib)
        weighted_symptoms TEXT,  -- JSON object (bobot gejala)
        description TEXT,
        skincare TEXT,  -- JSON array (rekomendasi skincare)
        disease_image TEXT
    )
    ''')

    # Tabel gejala
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS symptoms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        symptom_image TEXT
    )
    ''')

    # Relasi penyakit & gejala
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS disease_symptoms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disease_id INTEGER,
        symptom_id INTEGER,
        FOREIGN KEY (disease_id) REFERENCES diseases(id),
        FOREIGN KEY (symptom_id) REFERENCES symptoms(id)
    )
    ''')

    # Rekomendasi skincare
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS skincare_recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        product_image TEXT
    )
    ''')

    # Riwayat diagnosa
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

    # Tabel pengguna (user & admin)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT CHECK(role IN ('user', 'admin')) NOT NULL
    )
    ''')

    conn.commit()
    conn.close()
    print("Database berhasil dibuat!")

if __name__ == "__main__":
    create_database()
