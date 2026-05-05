from flask import request, jsonify
import sqlite3
from db import DB_PATH


def connect_db():
    return sqlite3.connect(DB_PATH)


def geri_bildirim_guncelle(id):
    try:
        data = request.get_json()

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE geri_bildirimler SET ad_soyad=?, tur=?, aciklama=? WHERE id=?",
            (data["ad_soyad"], data["tur"], data["aciklama"], id)
        )

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Geri bildirim güncellendi"
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500