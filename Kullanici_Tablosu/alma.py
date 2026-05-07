from flask import jsonify
from db import connect_db

def kullanicilari_listele():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM kullanicilar")
    data = cursor.fetchall()

    conn.close()
    return jsonify(data)

def kullanici_getir(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM kullanicilar WHERE id=?", (id,))
    data = cursor.fetchone()

    conn.close()
    return jsonify(data)