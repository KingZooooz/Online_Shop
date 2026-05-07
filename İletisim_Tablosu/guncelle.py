from flask import request, jsonify
from db import connect_db

def iletisim_guncelle(id):
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE iletisim
        SET adres=?, telefon=?, yetkili=?, email=?
        WHERE id=?
    """, (
        data["adres"],
        data["telefon"],
        data["yetkili"],
        data["email"],
        id
    ))

    conn.commit()
    conn.close()
    return jsonify({"mesaj": "İletişim güncellendi"})