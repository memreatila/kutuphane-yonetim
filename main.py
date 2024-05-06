from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtGui
from giris_ui import Ui_MainWindow
from kutuphane import Uye
from ana import AnaSayfa
from kayit import KayitSayfa
from veritabani import Veritabani

class arayuz(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtprogram = Ui_MainWindow()
        self.qtprogram.setupUi(self)
        self.qtprogram.girisButon.clicked.connect(self.girisyap)
        kayitsayfa = KayitSayfa()
        self.qtprogram.kayitButon.clicked.connect(lambda: kayitsayfa.show())

    def girisyap(self):
        kullaniciadi = self.qtprogram.adLine.text()
        sifre = self.qtprogram.sifreLine.text()
        Veritabani.query('SELECT * FROM kullanicilar WHERE kullaniciadi = ? AND sifre = ?', (kullaniciadi, sifre))
        sql = Veritabani.fetchone()

        if sql is None:
            QMessageBox.warning(self, "Giris", "Kullanıcı adı veya şifre yanlış.", QMessageBox.Ok)
            return

        uye = Uye(*sql)
        self.anasayfa = AnaSayfa(uye)
        self.anasayfa.show()
        self.close()


app = QApplication([])
pencere = arayuz()
pencere.show()
app.exec_()
