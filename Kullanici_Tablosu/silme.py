from flask import jsonify
from db import connect_db

def kullanici_sil(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM kullanicilar WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"mesaj": "Silindi"})