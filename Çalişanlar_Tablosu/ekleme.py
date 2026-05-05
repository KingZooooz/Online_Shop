from flask import request, jsonify
import sqlite3
from db import DB_PATH


def connect_db():
    return sqlite3.connect(DB_PATH)


def calisan_ekle():
    try:
        data = request.get_json()

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO adminler (ad, soyad, kullanici_adi, sifre) VALUES (?, ?, ?, ?)",
            (data["ad"], data["soyad"], data["kullanici_adi"], data["sifre"])
        )

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Admin eklendi"
        }), 201

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500