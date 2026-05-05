from flask import jsonify
import sqlite3
from db import DB_PATH


def connect_db():
    return sqlite3.connect(DB_PATH)


def urun_sil(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM urunler WHERE id=?", (id,))

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Ürün silindi"
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500