from flask import request, jsonify
from db import connect_db

def kullanici_guncelle(id):
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE kullanicilar 
        SET ad=?, soyad=?, telefon=?, email=?, adres=?, 
            kart_numarasi=?, kart_son_kullanim=?, kart_cvv=?
        WHERE id=?
    """, (
        data["ad"],
        data["soyad"],
        data["telefon"],
        data["email"],
        data["adres"],
        data["kart_numarasi"],
        data["kart_son_kullanim"],
        data["kart_cvv"],
        id
    ))

    conn.commit()
    conn.close()

    return jsonify({"mesaj": "Güncellendi"})