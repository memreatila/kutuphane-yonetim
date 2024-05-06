from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from kitapiade_ui import Ui_Form
from veritabani import Veritabani
from kutuphane import Odunc, Kitap

class KitapIadeSayfa(QWidget):
    kitap_iade_sinyal = pyqtSignal()
    def __init__(self, uye) -> None:
        super().__init__()
        self.kitapiadeform = Ui_Form()
        self.kitapiadeform.setupUi(self)
        self.kitapiadeform.iadeButon.clicked.connect(self.iade)
        self.uye = uye

    def goster(self):
        self.kitapiadeform.kitapBox.clear()
        Veritabani.query('SELECT kitap FROM oduncler WHERE uyeid = ?',(self.uye.id,))
        oduncler = Veritabani.fetchall()
        self.show()

        if oduncler is not None:
            for kitap in oduncler:
                self.kitapiadeform.kitapBox.addItem(kitap[0])

    def iade(self):        
        yanit = QMessageBox.warning(self, "Kitap İade", "Kitap iade işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        
        Veritabani.query('SELECT * FROM kitaplar WHERE ad = ?',(self.kitapiadeform.kitapBox.currentText(),))
        kitap = Veritabani.fetchone()
        
        kitapindex = self.kitapiadeform.kitapBox.currentIndex()
        
        self.kitapiadeform.kitapBox.removeItem(kitapindex)
        self.kitap_iade_sinyal.emit()

        odunc = Odunc(Kitap(*kitap), self.uye)
        odunc.iade()