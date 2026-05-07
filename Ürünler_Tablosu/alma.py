from flask import jsonify
from db import connect_db

def urunleri_listele():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM urunler")
    data = cursor.fetchall()

    conn.close()
    return jsonify(data)


def urun_getir(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM urunler WHERE id=?",
        (id,)
    )

    data = cursor.fetchone()

    conn.close()
    return jsonify(data)