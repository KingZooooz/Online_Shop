from flask import request, jsonify
from db import connect_db

def iletisim_ekle():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO iletisim (adres, telefon, yetkili, email)
        VALUES (?, ?, ?, ?)
    """, (
        data["adres"],
        data["telefon"],
        data["yetkili"],
        data["email"]
    ))

    conn.commit()
    conn.close()
    return jsonify({"mesaj": "İletişim eklendi"})