from flask import request, jsonify
import sqlite3
from db import DB_PATH


def connect_db():
    return sqlite3.connect(DB_PATH)


def geri_bildirim_ekle():
    try:
        data = request.get_json()

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO geri_bildirimler (ad_soyad, tur, aciklama) VALUES (?, ?, ?)",
            (data["ad_soyad"], data["tur"], data["aciklama"])
        )

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Geri bildirim eklendi"
        }), 201

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500