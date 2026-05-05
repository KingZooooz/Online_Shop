from flask import jsonify
import sqlite3
from db import DB_PATH


def connect_db():
    return sqlite3.connect(DB_PATH)


def calisanlari_listele():
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM calisanlar")
    rows = cursor.fetchall()

    conn.close()

    return jsonify({
        "success": True,
        "count": len(rows),
        "calisanlar": [dict(row) for row in rows]
    }), 200