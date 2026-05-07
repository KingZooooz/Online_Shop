from flask import jsonify
from db import connect_db

def iletisim_listele():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM iletisim")
    data = cursor.fetchall()

    conn.close()
    return jsonify(data)


def iletisim_getir(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM iletisim WHERE id=?", (id,))
    data = cursor.fetchone()

    conn.close()
    return jsonify(data)