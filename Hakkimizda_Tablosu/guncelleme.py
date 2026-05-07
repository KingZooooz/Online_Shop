from flask import request, jsonify
from db import connect_db

def hakkimizda_guncelle():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE hakkimizda
        SET vizyon=?, misyon=?, biz_kimiz=?, bize_katilin=?
        WHERE id=1
    """, (
        data["vizyon"],
        data["misyon"],
        data["biz_kimiz"],
        data["bize_katilin"]
    ))

    conn.commit()
    conn.close()
    return jsonify({"mesaj": "Güncellendi"})