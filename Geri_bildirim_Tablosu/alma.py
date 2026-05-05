from flask import jsonify
import sqlite3
from db import DB_PATH


def connect_db():
    return sqlite3.connect(DB_PATH)


def geri_bildirimleri_listele():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM geri_bildirimler")
    rows = cursor.fetchall()

    conn.close()

    return jsonify([dict(row) for row in rows])