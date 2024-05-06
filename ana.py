from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ana_ui import Ui_MainWindow
from PyQt5.QtGui import QIntValidator
from kutuphane import *
from PyQt5 import QtGui
from odunc import OduncSayfa
from kitapiade import KitapIadeSayfa
from veritabani import Veritabani

class AnaSayfa(QMainWindow):
    def __init__(self, uye) -> None:
        super().__init__()
        self.anasayfa = Ui_MainWindow()
        self.anasayfa.setupUi(self)
        self.index = 0
        self.uye = uye
        self.anasayfa.sonrakiButon.clicked.connect(self.sonrakikitap)
        self.anasayfa.oncekiButon.clicked.connect(self.oncekikitap)
        self.anasayfa.oduncButon.clicked.connect(self.oduncal)
        self.kitap_liste_guncelle()
        self.kitapguncelle()
        
        oduncsayfa = OduncSayfa(self.uye)
        self.anasayfa.oduncListe.triggered.connect(lambda: oduncsayfa.goster())

        kitapiadesayfa = KitapIadeSayfa(self.uye)
        self.anasayfa.iade.triggered.connect(lambda: kitapiadesayfa.goster())
        kitapiadesayfa.kitap_iade_sinyal.connect(self.kitap_liste_guncelle)

    def sonrakikitap(self):
        self.index += 1
        if len(self.kitaplar) == self.index:
            self.index = 0
        self.kitapguncelle()

    def oncekikitap(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.kitaplar)-1
        self.kitapguncelle()

    def kitapguncelle(self):
        kitap = self.kitaplar[self.index]
        self.anasayfa.foto.setPixmap(QtGui.QPixmap("Fotograflar/" + kitap.fotograf))
        self.anasayfa.aciklamaLabel.setText(kitap.aciklama)
        self.anasayfa.kitaplabel.setText(kitap.ad)
        self.anasayfa.yazarlabel.setText(kitap.yazar)

    def oduncal(self):
        kitap = self.kitaplar[self.index]
        if kitap.durum == 'Mevcut Değil':
            QMessageBox.warning(self, "Kitap", "Seçtiğiniz Kitap Mevcut Değildir.",QMessageBox.Ok)
            return
        
        yanit = QMessageBox.warning(self, "Kitap", "Bu kitabı ödünç alma işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        
        odunc = Odunc(kitap, self.uye)
        odunc.odunc_al()

        QMessageBox.information(self, "Kitap", "Ödünç alındı.", QMessageBox.Ok)

    def kitap_liste_guncelle(self):
        Veritabani.query('SELECT * FROM kitaplar')
        sql = Veritabani.fetchall()
        kitaplar = []
        for kayit in sql:
            kitaplar.append(Kitap(*kayit))
        self.kitaplar = kitaplar
