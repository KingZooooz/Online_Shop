from flask import jsonify
from db import connect_db

def faq_sil(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM faq WHERE id=?", (id,))

    conn.commit()
    conn.close()
    return jsonify({"mesaj": "FAQ silindi"})