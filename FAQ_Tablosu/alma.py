from flask import jsonify
from db import connect_db

def faq_listele():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faq")
    data = cursor.fetchall()

    conn.close()
    return jsonify(data)


def faq_getir(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faq WHERE id=?", (id,))
    data = cursor.fetchone()

    conn.close()
    return jsonify(data)