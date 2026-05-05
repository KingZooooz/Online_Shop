from flask import Flask
from flask_cors import CORS
from db import DB_PATH
app = Flask(__name__)
CORS(app)


from Ürünler_Tablosu.ekleme import urun_ekle
from Ürünler_Tablosu.alma import urunleri_listele
from Ürünler_Tablosu.guncelleme import urun_guncelle
from Ürünler_Tablosu.silme import urun_sil


from Çalişanlar_Tablosu.ekleme import calisan_ekle
from Çalişanlar_Tablosu.alma import calisanlari_listele
from Çalişanlar_Tablosu.guncelleme import calisan_guncelle
from Çalişanlar_Tablosu.silme import calisan_sil


from Geri_bildirim_Tablosu.ekleme import geri_bildirim_ekle
from Geri_bildirim_Tablosu.alma import geri_bildirimleri_listele
from Geri_bildirim_Tablosu.guncelleme import geri_bildirim_guncelle
from Geri_bildirim_Tablosu.silme import geri_bildirim_sil


app = Flask(__name__)
CORS(app, supports_credentials=True)

app.add_url_rule('/calisan_ekle', view_func=calisan_ekle, methods=['POST'])
app.add_url_rule('/calisan_listele', view_func=calisanlari_listele, methods=['GET'])
app.add_url_rule('/calisan_guncelle', view_func=calisan_guncelle, methods=['PUT'])
app.add_url_rule('/calisan_sil', view_func=calisan_sil, methods=['DELETE'])


app.add_url_rule('/urun_ekle', view_func=urun_ekle, methods=['POST'])
app.add_url_rule('/urunleri_listele', view_func=urunleri_listele, methods=['GET'])
app.add_url_rule('/urun_guncelle', view_func=urun_guncelle, methods=['PUT'])
app.add_url_rule('/urun_sil', view_func=urun_sil, methods=['DELETE'])

app.add_url_rule('/geri_bildirim_ekle', view_func=geri_bildirim_ekle, methods=['POST'])
app.add_url_rule('/geri_bildirim_listele', view_func=geri_bildirimleri_listele, methods=['GET'])
app.add_url_rule('/geri_bildirim_guncelle', view_func=geri_bildirim_guncelle, methods=['PUT'])
app.add_url_rule('/geri_bildirim_sil', view_func=geri_bildirim_sil, methods=['DELETE'])

if __name__ == "__main__":
    print("DB PATH:", DB_PATH)  
    app.run(port=5002, debug=True)