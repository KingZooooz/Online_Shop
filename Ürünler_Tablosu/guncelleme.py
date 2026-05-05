from flask import request, jsonify
import sqlite3
from db import DB_PATH


def connect_db():
    return sqlite3.connect(DB_PATH)


def urun_guncelle(id):
    try:
        data = request.get_json()

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE urunler SET urun_adi=?, urun_kodu=?, urun_aciklama=?, urun_numarasi=? WHERE id=?",
            (
                data["urun_adi"],
                data["urun_kodu"],
                data["urun_aciklama"],
                data["urun_numarasi"],
                id
            )
        )

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Ürün güncellendi"
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500