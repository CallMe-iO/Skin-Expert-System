from models.setup_database import create_tables
from config.db_config import get_db_connection  # <-- TAMBAHKAN INI
import json  # <-- TAMBAHKAN INI UNTUK HANDLE JSON

def initialize_database():
    # Membuat tabel
    create_tables()
    
    # Dapatkan koneksi database
    conn = get_db_connection()  # <-- SEKARANG SUDAH TERDEFINISI
    cursor = conn.cursor()
    
    # Tambah admin default
    cursor.execute('''
        INSERT INTO users (username, password, role)
        VALUES (?, ?, ?)
    ''', ('admin', 'admin123', 'admin'))
    
    # Tambah contoh gejala
    symptoms = [
        ('Kemerahan', 'Kulit tampak kemerahan', '/assets/symptoms/redness.jpg'),
        ('Gatal', 'Rasa gatal pada kulit', '/assets/symptoms/itch.jpg'),
        ('Bersisik', 'Kulit mengelupas', '/assets/symptoms/flaky.jpg')
    ]
    cursor.executemany('''
        INSERT INTO symptoms (name, description, image_path)
        VALUES (?, ?, ?)
    ''', symptoms)
    
    # Tambah contoh penyakit
    disease_data = (
        'Dermatitis',
        json.dumps([1, 2]),  # required_symptoms (IDs 1 dan 2)
        json.dumps({"1": 0.6, "2": 0.4}),  # weighted_symptoms
        'Peradangan kulit kronis',
        'Gunakan pelembab non-alergi 2x sehari',
        '/assets/diseases/dermatitis.jpg'
    )
    cursor.execute('''
        INSERT INTO diseases (name, required_symptoms, weighted_symptoms, 
                            description, skincare_recommendation, disease_image)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', disease_data)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully!")