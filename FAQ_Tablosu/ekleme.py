from flask import request, jsonify
from db import connect_db

def faq_ekle():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO faq (soru, cevap)
        VALUES (?, ?)
    """, (
        data["soru"],
        data["cevap"]
    ))

    conn.commit()
    conn.close()
    return jsonify({"mesaj": "FAQ eklendi"})