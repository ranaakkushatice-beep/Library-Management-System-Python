import sqlite3

# Veritabanı bağlantısı (Yoksa oluşturur)
db = sqlite3.connect('kutuphane.db')
cursor = db.cursor()

# SQL Tablosu oluşturma
cursor.execute('''
    CREATE TABLE IF NOT EXISTS kitaplar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isim TEXT NOT NULL,
        yazar TEXT NOT NULL,
        yil INTEGER
    )
''')

def kitap_ekle(isim, yazar, yil):
    cursor.execute("INSERT INTO kitaplar (isim, yazar, yil) VALUES (?, ?, ?)", (isim, yazar, yil))
    db.commit()
    print(f"\n✅ '{isim}' kütüphaneye eklendi!")

def kitaplari_listele():
    cursor.execute("SELECT * FROM kitaplar")
    kitaplar = cursor.fetchall()
    print("\n--- Kütüphane Listesi ---")
    for kitap in kitaplar:
        print(f"ID: {kitap[0]} | Kitap: {kitap[1]} | Yazar: {kitap[2]} | Yıl: {kitap[3]}")

# Test Çalıştırması
print("📚 Kütüphane Sistemine Hoş Geldiniz!")
kitap_ekle("Python ile Programlama", "Hatice Rana Akkuş", 2026)
kitap_ekle("Yapay Zekaya Giriş", "Mühendislik Dünyası", 2024)

kitaplari_listele()

db.close()