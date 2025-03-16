from config.db_config import get_db_connection
import json

# Fungsi untuk membuat tabel
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Tabel Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user'
        )
    ''')
    
    # Tabel Symptoms
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS symptoms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            image_path TEXT
        )
    ''')
    
    # Tabel Diseases
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS diseases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            required_symptoms TEXT,
            weighted_symptoms TEXT,
            description TEXT,
            skincare_recommendation TEXT NOT NULL,
            disease_image TEXT
        )
    ''')
    
    # Tabel History
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            symptoms TEXT NOT NULL,
            disease_id INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (disease_id) REFERENCES diseases(id)
        )
    ''')
    
    conn.commit()
    conn.close()

# ===================================================
# FUNGSI BARU YANG HARUS DITAMBAHKAN DI BAWAH INI
# ===================================================

# Fungsi untuk mengambil semua data dari tabel
def get_all(table_name: str):
    """Mengambil semua data dari tabel tertentu"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    results = cursor.fetchall()
    
    # Konversi ke list of dictionaries
    columns = [column[0] for column in cursor.description]
    data = [dict(zip(columns, row)) for row in results]
    
    conn.close()
    return data

# Fungsi untuk mengambil data berdasarkan ID
def get_by_id(table_name: str, id: int):
    """Mengambil data berdasarkan ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (id,))
    result = cursor.fetchone()
    
    if result:
        columns = [column[0] for column in cursor.description]
        data = dict(zip(columns, result))
    else:
        data = None
    
    conn.close()
    return data

# Fungsi untuk menambah gejala (contoh CRUD)
def add_symptom(name: str, description: str, image_path: str):
    """Menambahkan gejala baru ke database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO symptoms (name, description, image_path) VALUES (?, ?, ?)",
        (name, description, image_path)
    )
    conn.commit()
    conn.close()