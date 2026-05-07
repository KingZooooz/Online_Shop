from flask import Flask
from flask_cors import CORS
from db import DB_PATH
app = Flask(__name__)
CORS(app)


from Ürünler_Tablosu.ekleme import urun_ekle
from Ürünler_Tablosu.alma import urunleri_listele
from Ürünler_Tablosu.alma import urun_getir
from Ürünler_Tablosu.guncelleme import urun_guncelle
from Ürünler_Tablosu.silme import urun_sil

from Çalişanlar_Tablosu.ekleme import calisan_ekle
from Çalişanlar_Tablosu.alma import calisanlari_listele
from Çalişanlar_Tablosu.alma import calisan_getir
from Çalişanlar_Tablosu.guncelleme import calisan_guncelle
from Çalişanlar_Tablosu.silme import calisan_sil

from Geri_bildirim_Tablosu.ekleme import geri_bildirim_ekle
from Geri_bildirim_Tablosu.alma import geri_bildirimleri_listele
from Geri_bildirim_Tablosu.alma import geri_bildirim_getir
from Geri_bildirim_Tablosu.guncelleme import geri_bildirim_guncelle
from Geri_bildirim_Tablosu.silme import geri_bildirim_sil

from Kullanici_Tablosu.ekleme import kullanici_ekle
from Kullanici_Tablosu.alma import kullanicilari_listele
from Kullanici_Tablosu.alma import kullanici_getir
from Kullanici_Tablosu.guncelleme import kullanici_guncelle
from Kullanici_Tablosu.silme import kullanici_sil

from İletisim_Tablosu.ekleme import iletisim_ekle
from İletisim_Tablosu.alma import iletisim_listele
from İletisim_Tablosu.alma import iletisim_getir
from İletisim_Tablosu.guncelle import iletisim_guncelle
from İletisim_Tablosu.silme import iletisim_sil

from FAQ_Tablosu.ekleme import faq_ekle
from FAQ_Tablosu.alma import faq_listele
from FAQ_Tablosu.alma import faq_getir
from FAQ_Tablosu.guncelleme import faq_guncelle
from FAQ_Tablosu.silme import faq_sil

from Hakkimizda_Tablosu.ekleme import hakkimizda_ekle
from Hakkimizda_Tablosu.alma import hakkimizda_listele
from Hakkimizda_Tablosu.alma import hakkimizda_getir
from Hakkimizda_Tablosu.guncelleme import hakkimizda_guncelle
from Hakkimizda_Tablosu.silme import hakkimizda_silme

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.add_url_rule('/calisan_ekle', view_func=calisan_ekle, methods=['POST'])
app.add_url_rule('/calisan_listele', view_func=calisanlari_listele, methods=['GET'])
app.add_url_rule('/calisan_getir/<int:id>', view_func=calisan_getir, methods=['GET'])
app.add_url_rule('/calisan_guncelle', view_func=calisan_guncelle, methods=['PUT'])
app.add_url_rule('/calisan_sil', view_func=calisan_sil, methods=['DELETE'])

app.add_url_rule('/urun_ekle', view_func=urun_ekle, methods=['POST'])
app.add_url_rule('/urunleri_listele', view_func=urunleri_listele, methods=['GET'])
app.add_url_rule('/urun_getir/<int:id>', view_func=urun_getir, methods=['GET'])
app.add_url_rule('/urun_guncelle', view_func=urun_guncelle, methods=['PUT'])
app.add_url_rule('/urun_sil', view_func=urun_sil, methods=['DELETE'])

app.add_url_rule('/geri_bildirim_ekle', view_func=geri_bildirim_ekle, methods=['POST'])
app.add_url_rule('/geri_bildirim_listele', view_func=geri_bildirimleri_listele, methods=['GET'])
app.add_url_rule('/geri_getir/<int:id>', view_func=geri_bildirim_getir, methods=['GET'])
app.add_url_rule('/geri_bildirim_guncelle', view_func=geri_bildirim_guncelle, methods=['PUT'])
app.add_url_rule('/geri_bildirim_sil', view_func=geri_bildirim_sil, methods=['DELETE'])

app.add_url_rule('/kullanici_ekle', view_func=kullanici_ekle, methods=['POST'])
app.add_url_rule('/kullanicilari_listele', view_func=kullanicilari_listele, methods=['GET'])
app.add_url_rule('/kullanici_getir/<int:id>', view_func=kullanici_getir, methods=['GET'])
app.add_url_rule('/kullanici_guncelle/<int:id>', view_func=kullanici_guncelle, methods=['PUT'])
app.add_url_rule('/kullanici_sil/<int:id>', view_func=kullanici_sil, methods=['DELETE'])

app.add_url_rule('/iletisim_ekle', view_func=iletisim_ekle, methods=['POST'])
app.add_url_rule('/iletisim_listele', view_func=iletisim_listele, methods=['GET'])
app.add_url_rule('/iletisim_getir/<int:id>', view_func=iletisim_getir, methods=['GET'])
app.add_url_rule('/iletisim_guncelle/<int:id>', view_func=iletisim_guncelle, methods=['PUT'])
app.add_url_rule('/iletisim_sil/<int:id>', view_func=iletisim_sil, methods=['DELETE'])

app.add_url_rule('/faq_ekle', view_func=faq_ekle, methods=['POST'])
app.add_url_rule('/faq_listele', view_func=faq_listele, methods=['GET'])
app.add_url_rule('/faq_getir/<int:id>', view_func=faq_getir, methods=['GET'])
app.add_url_rule('/faq_guncelle/<int:id>', view_func=faq_guncelle, methods=['PUT'])
app.add_url_rule('/faq_sil/<int:id>', view_func=faq_sil, methods=['DELETE'])

app.add_url_rule("/hakkimizda_ekle", view_func=hakkimizda_ekle, methods=["POST"])
app.add_url_rule("/hakkimizda_listele", view_func=hakkimizda_listele, methods=["GET"])
app.add_url_rule('/hakkimizda_getir/<int:id>', view_func=hakkimizda_getir, methods=['GET'])
app.add_url_rule("/hakkimizda_guncelle/<int:id>", view_func=hakkimizda_guncelle, methods=["PUT"])
app.add_url_rule("/hakkimizda_sil/<int:id>", view_func=hakkimizda_silme, methods=["DELETE"])


if __name__ == "__main__":
    print("DB PATH:", DB_PATH)  
    app.run(port=5002, debug=True)