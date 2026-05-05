from flask import jsonify
import sqlite3
from db import DB_PATH


def connect_db():
    return sqlite3.connect(DB_PATH)


def geri_bildirim_sil(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM geri_bildirimler WHERE id=?", (id,))

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Geri bildirim silindi"
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500