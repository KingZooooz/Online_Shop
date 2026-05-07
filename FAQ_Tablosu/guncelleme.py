from flask import request, jsonify
from db import connect_db

def faq_guncelle(id):
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE faq
        SET soru=?, cevap=?
        WHERE id=?
    """, (
        data["soru"],
        data["cevap"],
        id
    ))

    conn.commit()
    conn.close()
    return jsonify({"mesaj": "FAQ güncellendi"})