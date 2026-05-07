from flask import jsonify
from db import connect_db

def hakkimizda_silme():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM hakkimizda WHERE id=?", (id,))

    conn.commit()
    conn.close()
    return jsonify({"mesaj": "Silindi"})