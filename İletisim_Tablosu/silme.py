from flask import request, jsonify
from db import connect_db

def iletisim_sil(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM iletisim WHERE id=?", (id,))

    conn.commit()
    conn.close()
    return jsonify({"mesaj": "İletişim silindi"})