from flask import request, jsonify
from db import connect_db

def kullanici_ekle():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO kullanicilar 
        (ad, soyad, telefon, email, adres, kart_numarasi, kart_son_kullanim, kart_cvv)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["ad"],
        data["soyad"],
        data["telefon"],
        data["email"],
        data["adres"],
        data["kart_numarasi"],
        data["kart_son_kullanim"],
        data["kart_cvv"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"mesaj": "Kullanıcı eklendi"})