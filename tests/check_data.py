import sqlite3

def check_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM diseases")
    diseases = cursor.fetchall()
    print("\nData Penyakit:")
    for d in diseases:
        print(d)

    cursor.execute("SELECT * FROM symptoms")
    symptoms = cursor.fetchall()
    print("\nData Gejala:")
    for s in symptoms:
        print(s)

    conn.close()

if __name__ == "__main__":
    check_data()
