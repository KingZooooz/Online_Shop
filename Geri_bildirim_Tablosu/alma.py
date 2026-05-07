from flask import jsonify
from db import connect_db

def geri_bildirimleri_listele():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM geri_bildirimler")
    data = cursor.fetchall()

    conn.close()
    return jsonify(data)


def geri_bildirim_getir(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM geri_bildirimler WHERE id=?", (id,))
    data = cursor.fetchone()

    conn.close()
    return jsonify(data)