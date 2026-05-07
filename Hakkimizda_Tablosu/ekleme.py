from flask import request, jsonify
from db import connect_db

def hakkimizda_ekle():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO hakkimizda (vizyon, misyon, biz_kimiz, bize_katilin)
        VALUES (?, ?, ?, ?)
    """, (
        data["vizyon"],
        data["misyon"],
        data["biz_kimiz"],
        data["bize_katilin"]
    ))

    conn.commit()
    conn.close()
    return jsonify({"mesaj": "Hakkımızda eklendi"})