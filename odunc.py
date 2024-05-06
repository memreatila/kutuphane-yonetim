from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from odunc_ui import Ui_Form
from PyQt5 import QtCore
from datetime import datetime
from veritabani import Veritabani

class OduncSayfa(QWidget):
    def __init__(self, uye) -> None:
        super().__init__()
        self.oduncform = Ui_Form()
        self.oduncform.setupUi(self)
        self.uye = uye

    def goster(self):
        tablo = self.oduncform.oduncTable
        tablo.setRowCount(0)
        Veritabani.query('SELECT kitap, tarih FROM oduncler WHERE uyeid = ?', (self.uye.id,))
        oduncler = Veritabani.fetchall()
        self.show()
        if oduncler is None:
            return
        tablo.setRowCount(len(oduncler))
        satir = 0
        tablo.setColumnWidth(0, 100)
        tablo.setColumnWidth(1, 140)
        tablo.setColumnWidth(2, 80)

        for kitap, tarih in oduncler:
            uyecell = QTableWidgetItem(self.uye.ad + " " + self.uye.soyad)
            kitapcell = QTableWidgetItem(kitap)
            tarihcell = QTableWidgetItem(datetime.strptime(tarih, "%Y-%m-%d").strftime("%d.%m.%Y"))

            #Hepsinin yazısını ortala
            uyecell.setTextAlignment(QtCore.Qt.AlignCenter)
            kitapcell.setTextAlignment(QtCore.Qt.AlignCenter)
            tarihcell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, uyecell)
            tablo.setItem(satir, 1, kitapcell)
            tablo.setItem(satir, 2, tarihcell)
            
            satir+=1

        #tablo.resizeColumnsToContents()
