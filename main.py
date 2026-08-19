import sqlite3

def main():
    print("Tebrikler! Yapay Zeka proje ortamın başarıyla kuruldu ve çalışıyor.")
    
    # Belgeleri saklayacağımız SQLite veritabanının kurulumu
    conn = sqlite3.connect('knowledge_base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            embedding TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Veritabanı ve 'documents' tablosu da sorunsuz hazırlandı!")

if __name__ == "__main__":
    main()