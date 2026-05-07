from flask import jsonify
from db import connect_db


def hakkimizda_listele():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM hakkimizda LIMIT 1")
    data = cursor.fetchone()

    conn.close()
    return jsonify(data)


def hakkimizda_getir(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM hakkimizda WHERE id=?", (id,))
    data = cursor.fetchone()

    conn.close()
    return jsonify(data)