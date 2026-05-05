from flask import request, jsonify
import sqlite3
from db import DB_PATH

def connect_db():
    return sqlite3.connect(DB_PATH)


def calisan_guncelle(id):
    try:
        data = request.get_json()

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE adminler SET ad=?, soyad=?, kullanici_adi=?, sifre=? WHERE id=?",
            (data["ad"], data["soyad"], data["kullanici_adi"], data["sifre"], id)
        )

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Çalışan güncellendi"
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500